#!/usr/bin/env python3

# Stworzyć i wyświetlić sygnał sinusoidalny

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 2, 0.01)
y = np.sin(2 * x * np.pi)

plt.plot(x, y)
plt.show()
