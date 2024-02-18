# Wczytać plik .wav i wyświetlić przebieg czasowy i FFT

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

# read audio samples
_, audio = read("mono.wav")

# plot the first 1024 samples
plt.plot(audio)
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()

audio_fft = np.fft.fft(audio)

plt.plot(np.abs(audio_fft)[:len(audio_fft) // 2])
plt.show()
