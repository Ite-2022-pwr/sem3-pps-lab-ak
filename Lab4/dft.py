import numpy as np


def dft(x):
    """Dyskretna transformata Fouriera"""
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)

    return np.dot(e, x)
