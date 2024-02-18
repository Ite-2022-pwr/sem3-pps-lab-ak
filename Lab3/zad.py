#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def dft(x):
    """Dyskretna transformata Fouriera"""
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)

    return np.dot(e, x)

fs = 100
t = np.arange(0, 1, 1 / fs)
s = 3 * np.sin(2 * np.pi * t * 5)
s += np.sin(2 * np.pi * t * 7)
s += 0.5 * np.sin(2 * np.pi * t * 3)

X = dft(s)
N = len(X)
n = np.arange(N)
T = N / fs
freq = n / T
freq_left = freq[:N // 2]
X_left = X[:N // 2]

plt.stem(freq_left, np.abs(X_left), 'b', markerfmt=" ", basefmt="-b")
plt.show()
