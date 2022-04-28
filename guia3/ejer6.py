import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def ejer_6():
  samplerate, data = wavfile.read('/home/axel/Documents/fich/PDS/src/datasets/escala.wav')
  print(data)

  plt.plot(data)
  plt.show()