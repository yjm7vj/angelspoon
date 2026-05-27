import numpy as np
from app.signal_processing import butterworth_bandpass_filter, dominant_frequency


def extract_features(df, sample_rate: int = 100):
    """
    Converts raw IMU data into model-ready features.
    """
    accel_x = df["accel_x"].values
    accel_y = df["accel_y"].values
    accel_z = df["accel_z"].values

    filtered_x = butterworth_bandpass_filter(accel_x, sample_rate)

    features = {
        "accel_x_mean": float(np.mean(accel_x)),
        "accel_x_std": float(np.std(accel_x)),
        "accel_y_std": float(np.std(accel_y)),
        "accel_z_std": float(np.std(accel_z)),
        "gyro_x_std": float(np.std(df["gyro_x"].values)),
        "gyro_y_std": float(np.std(df["gyro_y"].values)),
        "gyro_z_std": float(np.std(df["gyro_z"].values)),
        "dominant_frequency": dominant_frequency(filtered_x, sample_rate),
        "signal_energy": float(np.sum(filtered_x ** 2)),
        "peak_amplitude": float(np.max(np.abs(filtered_x)))
    }

    return features
