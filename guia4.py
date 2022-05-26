import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal

def ejer1():
  f1 = 10
  f2 = 20
  s = senoidal(0,1,1000,f1)[1]+(4*senoidal(0,1,1000,f2)[1])+4
  
  N = s.shape[0]
  S = np.fft.fft(s)
  # pasamos la parte de las frecuencias negativas adelante
  S = np.concatenate((S[int((N)/2):], S[:int((N)/2)]))

  # condicion de perceval
  print(sum(s**2))
  print((1/N)*sum(abs(S)**2))

  # plots
  fig,ax = plt.subplots(2,1)
  ax[0].stem(s)
  ax[1].stem(abs(S))
  plt.show()

if __name__=="__main__":
  ejer1()