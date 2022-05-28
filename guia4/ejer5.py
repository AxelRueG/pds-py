import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal
from guia4.fft import my_fft_f

def ejer5():
  t,x = senoidal(0,1,50,27)
  # X = np.fft.fft(x)
  f,X = my_fft_f(x,50)
  fig,ax = plt.subplots(2)
  ax[0].stem(t,x)
  ax[1].stem(f,abs(X))
  plt.show()