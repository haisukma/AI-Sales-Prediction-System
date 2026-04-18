from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predict import predict_sales_status
from sales import get_sales_data

app = FastAPI(title="AI Sales Prediction System API")

class PredictionRequest(BaseModel):
    jumlah_penjualan: int
    harga: float
    diskon: float

class PredictionResponse(BaseModel):
    prediction: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/sales")
def get_sales():
    try:
        data = get_sales_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        result = predict_sales_status(
            request.jumlah_penjualan,
            request.harga,
            request.diskon
        )
        return {"prediction": result}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))