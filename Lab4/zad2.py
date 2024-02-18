#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import time

from dft import dft


fs = 100
t = np.arange(0, 1, 1 / fs)
s = 3 * np.sin(2 * np.pi * t * 5)
s += np.sin(2 * np.pi * t * 7)
s += 0.5 * np.sin(2 * np.pi * t * 3)

# DFT
start = time.perf_counter()
dft(s)
stop = time.perf_counter()
print(f"DFT: {stop - start}")

# FFT
start = time.perf_counter()
np.fft.fft(s)
stop = time.perf_counter()
print(f"FFT: {stop - start}")
