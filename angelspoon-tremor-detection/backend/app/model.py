from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "tremor_model.joblib"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run python train_model.py first.")
    return joblib.load(MODEL_PATH)


def predict_tremor(features: dict):
    model = load_model()
    input_df = pd.DataFrame([features])
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    return {
        "tremor_detected": bool(prediction),
        "tremor_probability": round(probability, 4),
        "severity_score": round(probability * 100, 2)
    }
