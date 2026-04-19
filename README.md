# AI Sales Prediction System

Mini fullstack system untuk:

* Mengelola data penjualan
* Memprediksi status produk (**Laris / Tidak Laris**)
* Menampilkan hasil dalam dashboard sederhana

---

## Tech Stack

### Frontend

* React JS
* Axios

### Backend

* FastAPI
* JWT Authentication

### Machine Learning

* Scikit-learn (Random Forest)
* Pandas & NumPy
* Joblib

---

## Project Structure

```
AI-Sales-Prediction-System/
│
├── backend/
│   ├── main.py
│   ├── predict.py
│   ├── sales.py
│   ├── requirements.txt
│   ├── scaler.pkl
│   └── model.pkl
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── data/
│   └── sales_data.csv
│
└── README.md
```

---

## System Architecture

### Komponen:

1. **Frontend (React)**

   * Menampilkan dashboard
   * Mengirim request ke backend

2. **Backend (FastAPI)**

   * Menyediakan REST API
   * Handle authentication (JWT)
   * Menghubungkan ke model ML

3. **Machine Learning**

   * Model Random Forest Classifier
   * Digunakan untuk klasifikasi status produk (Laris / Tidak)
   * Memanfaatkan fitur:
     - jumlah_penjualan
     - harga
     - diskon
   * Model disimpan dalam file `.pkl` dan di-load saat inference

4. **Data Source**

   * CSV file (sales_data.csv)

---

## Alur Data

1. User login melalui frontend
2. Backend mengembalikan JWT token
3. Frontend menyimpan token
4. User membuka dashboard → frontend call `/sales`
5. Backend membaca CSV → kirim data ke frontend
6. User input data → klik predict
7. Frontend kirim ke `/predict` dengan token
8. Backend:

   * validasi token
   * load model Random Forest
   * preprocessing (scaling)
   * melakukan prediksi
9. Hasil dikirim ke frontend
10. Frontend menampilkan hasil ke user

---

## Diagram (Simple)

```
[ React Frontend ] --> (API Call) --> [ FastAPI Backend ] --> [ CSV ] dan [ ML Model ]
```

## Cara Menjalankan

### 1. Backend

```bash
python -m venv venv
Aktifkan venv di windows:
venv\Scripts\activate 
Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Akses API:

```
http://127.0.0.1:8000/docs
```

---

### 2. Frontend

```bash
cd frontend
npm install
npm start
```

Akses:

```
http://localhost:3000
```

---

## Authentication

Gunakan dummy login:

```
username: admin
password: admin
```

---

## API Endpoint

### POST /login

Login untuk mendapatkan JWT token

### GET /sales

Mengambil data penjualan dari CSV

### POST /predict

Prediksi status produk

Request:

```json
{
  "jumlah_penjualan": 100,
  "harga": 50000,
  "diskon": 10
}
```

Response:

```json
{
  "prediction": "Laris"
}
```

---

## Machine Learning

* Problem: Classification
* Model: Random Forest
* Features:

  * jumlah_penjualan
  * harga
  * diskon

### Insight:

Model sangat dipengaruhi oleh `jumlah_penjualan`, yang memiliki korelasi kuat terhadap label.

---

## Fitur Utama

* Login dengan JWT Authentication
* Dashboard data penjualan
* Prediksi status produk
* Load more

---

## Design Decision

* Menggunakan FastAPI karena ringan dan cepat untuk REST API
* Memisahkan backend, frontend, dan ML untuk scalability
* Menggunakan Random Forest karena model ini mampu menangkap hubungan non-linear antar fitur dan robust terhadap variasi data. Selain itu, Random Forest juga menyediakan feature importance yang membantu dalam memahami kontribusi masing-masing fitur terhadap prediksi
* Menggunakan Load More untuk meningkatkan performa UI

---

## Asumsi

* Data berasal dari CSV (tidak real-time database)
* User hanya 1 (dummy authentication)
* Model tidak di-train ulang secara otomatis

---

## Future Improvement

* Tambah database (PostgreSQL / MySQL)
* Model retraining otomatis
* Dashboard analytics (chart)
* Role-based authentication

---
