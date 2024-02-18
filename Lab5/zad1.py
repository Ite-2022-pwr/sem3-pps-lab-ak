# Dla sygnału złożonego z 3 sin zastosować filtr dolnoprzepustowy. Wyświetlić FFT przed i po filtracji

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


def lowpass_filter(sig, cutoff, fs):
    b, a = signal.butter(6, cutoff, btype='lowpass', analog=False, fs=fs)
    return signal.lfilter(b, a, sig)


fs = 100
t = np.arange(0, 1, 1 / fs)
s = np.sin(2 * np.pi * t * 5)
s += np.sin(2 * np.pi * t * 7)
s += np.sin(2 * np.pi * t * 3)

# plt.plot(t, s)
# plt.show()

fft = np.fft.fft(s)
freq = np.fft.fftfreq(len(s), 1/fs)

# plt.plot(t, fft)
# plt.show()

filtered = lowpass_filter(s, 0.7, fs)

# plt.plot(t, filtered)
# plt.show()

filtered_fft = np.fft.fft(filtered)

# plt.plot(t, filtered_fft)
# plt.show()

N = len(freq)
freq_left = freq[:N // 2]

plt.stem(freq_left, np.abs(fft[:N // 2]), 'b', markerfmt=" ", basefmt="-b")
plt.show()

plt.stem(freq_left, np.abs(filtered_fft[:N // 2]), 'b', markerfmt=" ", basefmt="-b")
plt.show()
