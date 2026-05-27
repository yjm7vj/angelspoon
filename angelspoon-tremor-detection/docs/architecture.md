# AngelSpoon Architecture

## Overview

AngelSpoon is designed as a software prototype for tremor detection in an assistive eating utensil.

## System Flow

1. **IMU Simulator**
   - Generates accelerometer and gyroscope data at 100 Hz.
   - Simulates normal motion, tremor motion, and sensor noise.

2. **Signal Processing**
   - Uses Butterworth band-pass filtering.
   - Uses FFT to identify dominant tremor frequencies.

3. **Feature Extraction**
   - Extracts statistical and frequency-domain features.
   - Converts raw sensor streams into ML-ready inputs.

4. **Machine Learning**
   - Trains Random Forest and SVM models.
   - Predicts tremor presence and severity.

5. **Backend API**
   - FastAPI exposes simulation, processing, and prediction endpoints.

6. **Dashboard**
   - React dashboard concept displays real-time sensor analytics.

## Future Improvements

- Connect real IMU hardware such as MPU-6050 or Arduino Nano 33 BLE Sense
- Add PostgreSQL persistence for sensor readings and predictions
- Stream live data using WebSockets
- Add model comparison dashboard
- Deploy backend on Render or Railway
- Deploy frontend on Vercel
