import numpy as np
import matplotlib.pyplot as plt
from guia4.fft import my_fft_f
from os.path import abspath

def ejer6():
  # datos conocidos
  fm = 360
  # electrocardiograma
  path = abspath('./datasets/necg.txt')
  data = np.loadtxt(path) # aparentemente tengo que usar la ruta entera
  N = len(data)
  # limpieza
  f,S = my_fft_f(data,fm)
  index = np.where(np.logical_and(abs(f)>40,abs(f)<180))
  S[index] = 0
  S = np.concatenate(( S[int(N/2):],S[:int(N/2)] )) # reordenamos para antitransformar
  s = np.fft.ifft(S)

  # graficas
  fig, ax = plt.subplots(2,constrained_layout=True)
  ax[0].plot(data)
  ax[0].set_title('senial original')
  ax[0].set_xlabel('tiempo [s]')
  ax[0].set_ylabel('x[n]')
  ax[1].plot(np.real(s))
  ax[1].set_title('senial sin ruido')
  ax[1].set_xlabel('tiempo [s]')
  ax[1].set_ylabel('x[n]')
  plt.show()

