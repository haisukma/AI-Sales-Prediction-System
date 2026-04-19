import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'sales_data.csv')

print("PATH:", DATA_PATH)

def get_sales_data():
    df = pd.read_csv(DATA_PATH)
    data = df.to_dict(orient='records')
    return data