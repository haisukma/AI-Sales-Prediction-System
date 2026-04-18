import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = '/Users/diajeng/Documents/AI-Sales-Prediction-System/data/sales_data.csv'

def get_sales_data():
    df = pd.read_csv(DATA_PATH)
    data = df.to_dict(orient='records')
    return data