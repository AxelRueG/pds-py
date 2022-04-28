import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal

import time # esto lo utilizo para ver el rendimiento

def parecido(fs,data):
  phis = np.arange(0, 2*np.pi, 0.1)
  M = np.zeros([phis.size,data.size])
  
  # @TODO testear la velocidad de esto contra toda la comparacion dentro del for
  for i in range(0,phis.size): 
    _, s = senoidal(0,1,data.size,fs,phis[i])
    M[i,:] = s
  parecido = np.dot(M,data)

  return max(parecido)

def ejer_5():
  data = np.loadtxt('/home/axel/Documents/fich/PDS/src/datasets/te.txt')

  filas = np.array([697, 770, 852, 941])
  columnas = np.array([1207, 1336, 1477])

  ini = time.time()
  maxval = parecido(filas[0],data[17200:21800])
  fin = time.time()
  print(f'time: {fin-ini}')
  print(maxval)

  # plt.plot(data)
  # plt.show()

''' INTERVALOS
[[ 17200,  21800 ],
 [ 30000,  35000 ],
 [ 39700,  43600 ],
 [ 48200,  53300 ],
 [ 59000,  63500 ],
 [ 69800,  74600 ],
 [ 80500,  85500 ]]
'''