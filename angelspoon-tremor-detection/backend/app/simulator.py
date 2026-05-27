import numpy as np
import pandas as pd


def generate_imu_data(duration_seconds: int = 10, sample_rate: int = 100, tremor: bool = True) -> pd.DataFrame:
    """
    Generates simulated IMU accelerometer and gyroscope data.
    sample_rate=100 means 100 sensor readings per second.
    """
    total_samples = duration_seconds * sample_rate
    time = np.linspace(0, duration_seconds, total_samples)

    normal_motion = 0.3 * np.sin(2 * np.pi * 1.2 * time)
    noise = np.random.normal(0, 0.08, total_samples)

    if tremor:
        # Parkinsonian resting tremor often appears around 4-6 Hz.
        tremor_signal = 0.7 * np.sin(2 * np.pi * 5.0 * time)
        label = 1
    else:
        tremor_signal = 0
        label = 0

    accel_x = normal_motion + tremor_signal + noise
    accel_y = 0.5 * normal_motion + 0.6 * tremor_signal + noise
    accel_z = 0.2 * normal_motion + 0.4 * tremor_signal + noise

    gyro_x = 0.8 * accel_x + np.random.normal(0, 0.05, total_samples)
    gyro_y = 0.8 * accel_y + np.random.normal(0, 0.05, total_samples)
    gyro_z = 0.8 * accel_z + np.random.normal(0, 0.05, total_samples)

    return pd.DataFrame({
        "time": time,
        "accel_x": accel_x,
        "accel_y": accel_y,
        "accel_z": accel_z,
        "gyro_x": gyro_x,
        "gyro_y": gyro_y,
        "gyro_z": gyro_z,
        "tremor_label": label
    })
