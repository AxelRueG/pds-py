import numpy as np
import matplotlib.pyplot as plt
from guia4.fft import my_fft_f

def ejer6():
  # datos conocidos
  fm = 360
  # electrocardiograma
  data = np.loadtxt('c:/Users/Bruno/Desktop/asd/pds-py/datasets/necg.txt') # aparentemente tengo que usar la ruta entera
  N = len(data)
  # limpieza
  f,S = my_fft_f(data,fm)
  index = np.where(np.logical_and(abs(f)>40,abs(f)<180))
  S[index] = 0
  S = np.concatenate(( S[int(N/2):],S[:int(N/2)] )) # reordenamos para antitransformar
  s = np.fft.ifft(S)

  # graficas
  fig, ax = plt.subplots(2)
  ax[0].plot(data)
  ax[1].plot(np.real(s))
  plt.show()

