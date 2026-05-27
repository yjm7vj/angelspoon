from fastapi import FastAPI
from app.simulator import generate_imu_data
from app.feature_extraction import extract_features
from app.model import predict_tremor

app = FastAPI(title="AngelSpoon Tremor Detection API")


@app.get("/")
def root():
    return {
        "project": "AngelSpoon Tremor Detection Platform",
        "status": "running"
    }


@app.get("/simulate")
def simulate(duration_seconds: int = 10, sample_rate: int = 100, tremor: bool = True):
    df = generate_imu_data(duration_seconds, sample_rate, tremor)
    return df.head(20).to_dict(orient="records")


@app.get("/process-signal")
def process_signal(duration_seconds: int = 10, sample_rate: int = 100, tremor: bool = True):
    df = generate_imu_data(duration_seconds, sample_rate, tremor)
    features = extract_features(df, sample_rate)
    return features


@app.get("/predict-tremor")
def predict(duration_seconds: int = 10, sample_rate: int = 100, tremor: bool = True):
    df = generate_imu_data(duration_seconds, sample_rate, tremor)
    features = extract_features(df, sample_rate)
    prediction = predict_tremor(features)

    return {
        "features": features,
        "prediction": prediction
    }
