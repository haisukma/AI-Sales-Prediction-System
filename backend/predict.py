import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_sales_status(jumlah_penjualan, harga, diskon):
    if jumlah_penjualan < 0:
        raise ValueError("jumlah_penjualan tidak boleh negatif")
    if harga < 0:
        raise ValueError("harga tidak boleh negatif")
    if not (0 <= diskon <= 100):
        raise ValueError("diskon harus antara 0-100")
    
    data = np.array([[jumlah_penjualan, harga, diskon]])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]

    return "Laris" if prediction == 1 else "Tidak"

# if __name__ == "__main__":
#     result = predict_sales_status(10, 50000, 100)
#     print("Prediction:", result)