import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')

df = pd.read_csv('/Users/diajeng/Documents/AI-Sales-Prediction-System/data/sales_data.csv')

df['status'] = df['status'].map({'Laris': 1, 'Tidak': 0})

X = df[['jumlah_penjualan', 'harga', 'diskon']]
y = df['status']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(
    random_state=42,
    class_weight='balanced',
    max_depth=5
)

model.fit(X_train, y_train)

feature_importance = pd.Series(
    model.feature_importances_,
    index=['jumlah_penjualan', 'harga', 'diskon']
)

print("\nFeature Importance:")
print(feature_importance.sort_values(ascending=False))

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)

print(f"Model saved to: {MODEL_PATH}")
print(f"Scaler saved to: {SCALER_PATH}")