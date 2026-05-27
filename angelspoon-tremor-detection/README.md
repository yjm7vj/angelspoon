# AngelSpoon Tremor Detection Platform

AngelSpoon is a software prototype for a Parkinson's assistive eating utensil.  
The platform simulates IMU sensor data, processes tremor-motion signals, trains machine learning models, and visualizes real-time tremor analytics.

## Project Highlights

- Built Python IMU simulator processing 100+ sensor readings per second
- Applied FFT and Butterworth filtering with SciPy for tremor-motion signal processing
- Trained Random Forest and SVM models for tremor detection
- Developed FastAPI backend for simulation, signal processing, and prediction endpoints
- Designed React dashboard concept for real-time tremor metrics and sensor analytics

## Tech Stack

Python, FastAPI, NumPy, SciPy, scikit-learn, pandas, PostgreSQL, React, Recharts

## Repository Structure

```text
angelspoon-tremor-detection/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── simulator.py
│   │   ├── signal_processing.py
│   │   ├── feature_extraction.py
│   │   └── model.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── data/
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/TremorDashboard.jsx
│   └── package.json
└── docs/
    └── architecture.md
```

## How It Works

1. The IMU simulator generates accelerometer and gyroscope readings.
2. Signal processing filters noise and isolates tremor frequencies.
3. Feature extraction calculates amplitude, variance, and dominant frequency.
4. A machine learning model predicts whether tremor is present.
5. The dashboard displays tremor analytics in a recruiter-friendly interface.

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python train_model.py
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Resume Bullet

Engineered ML-powered tremor detection platform for Parkinson's assistive utensil prototype using Python, SciPy, scikit-learn, FastAPI, PostgreSQL, and React.
