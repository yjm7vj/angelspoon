import numpy as np
from scipy.signal import butter, filtfilt
from scipy.fft import rfft, rfftfreq


def butterworth_bandpass_filter(signal, sample_rate: int = 100, lowcut: float = 3.0, highcut: float = 8.0, order: int = 4):
    """
    Filters the signal to focus on tremor-like frequencies.
    Parkinsonian tremor is commonly analyzed around the 3-8 Hz range.
    """
    nyquist = 0.5 * sample_rate
    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, signal)


def dominant_frequency(signal, sample_rate: int = 100):
    """
    Uses FFT to identify the strongest frequency in a signal.
    """
    yf = np.abs(rfft(signal))
    xf = rfftfreq(len(signal), 1 / sample_rate)

    if len(yf) <= 1:
        return 0

    index = np.argmax(yf[1:]) + 1
    return float(xf[index])
