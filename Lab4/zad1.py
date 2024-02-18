#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from dft import dft


fs = 100
t = np.arange(0, 1, 1 / fs)
s = 3 * np.sin(2 * np.pi * t * 5)
s += np.sin(2 * np.pi * t * 7)
s += 0.5 * np.sin(2 * np.pi * t * 3)

plt.plot(t, s)
plt.show()

X = dft(s)
N = len(X)
n = np.arange(N)
T = N / fs
freq = n / T
freq_left = freq[:N // 2]
X_left = X[:N // 2]

plt.stem(freq_left, np.abs(X_left), 'b', markerfmt=" ", basefmt="-b")
plt.show()

plt.specgram(s, Fs=fs)
plt.show()
