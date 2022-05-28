import numpy as np
import matplotlib.pyplot as plt
from guia4.fft import my_fft
from ventanas import bartlett, hanning, rectangular

def ejer4():
  W = bartlett(10)
  w = np.zeros(30)
  w[10:20] = W 
  fig, ax = plt.subplots(2)
  ax[0].plot(w)
  Wk = my_fft(w[15:])
  # Wk = my_fft(w)
  ax[1].plot(abs(Wk))
  plt.show()
