from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from backend.predict import predict_sales_status
from backend.sales import get_sales_data
from dotenv import load_dotenv
import os

app = FastAPI(title="AI Sales Prediction System API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class LoginRequest(BaseModel):
    username: str
    password: str

class PredictionRequest(BaseModel):
    jumlah_penjualan: int
    harga: float
    diskon: float

class PredictionResponse(BaseModel):
    prediction: str

@app.get("/")
def root():
    return {"message": "API is running"}

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "admin":
        payload = {
            "sub": request.username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {
            "access_token": token,
            "token_type": "bearer"
        }
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/sales")
def get_sales():
    try:
        data = get_sales_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest, token: str = Depends(verify_token)):
    try:
        result = predict_sales_status(
            request.jumlah_penjualan,
            request.harga,
            request.diskon
        )
        return {"prediction": result}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))