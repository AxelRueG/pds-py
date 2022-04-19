import numpy as np 
import matplotlib.pyplot as plt
from Signals import cuadrada, senoidal
from convolucion import convolucion_circular, convolucion_lineal
from sistemas import respuesta_al_impulso, delta_dirac

def ejer1_sistemas ():
  # ejercicio 1 _______________________________________________________________
  # item 1
  fm = 50
  t,xn = cuadrada(0,1,fm)
  w = 2*np.pi*2*np.arange(0,t.size)
  gn = 2*np.sin(w*1/fm)
  y = gn*xn  

  fig,axs = plt.subplots(3,1)
  axs[0].stem(t,xn)
  axs[1].stem(t,gn)
  axs[2].stem(t,y)
  plt.show()

def ejer4_sistemas():
  y1 = respuesta_al_impulso(25, np.array([1]), np.array([-1]))
  y2 = respuesta_al_impulso(25, np.array([1,0.5]), np.array([0]))
  y3 = respuesta_al_impulso(25, np.array([1]), np.array([0.5,-0.25]))

  # graficas
  fig, axs = plt.subplots(3,1)
  axs[0].stem(y1)
  axs[1].stem(y2)
  axs[2].stem(y3)
  plt.show()


def ejer1y2_convolucion(x,h):
  yl = convolucion_lineal(x,h)
  yc = convolucion_circular(x,h)
  
  fig, ax = plt.subplots(2)
  fig.suptitle('convolucion lineal y circular')
  ax[0].stem(yl)
  ax[1].stem(yc)
  plt.show()


def ejer3_convolucion(a,N):
  n = np.arange(0,N)
  x = delta_dirac(N)-(a*delta_dirac(N,1))
  ha = np.sin(8*n)
  hb = a**n

  # sistema en cascada
  y1 = convolucion_lineal(x,ha)
  y = convolucion_lineal(y1,hb)

  # resultados
  print(y.size)

  fig, ax = plt.subplots(2,1)
  ax[0].stem(y1)
  ax[1].stem(y)
  plt.show()



if __name__ == '__main__':  
# SISTEMAS -------------------------------------------------------------------
  # ejer1_sistemas()
  # ejer4_sistemas()
# CONVOLUCION ----------------------------------------------------------------
  ejer1y2_convolucion(
    np.array([0.5,1,1,0.5,0,-0.5,-1,-1,-0.5,0]),
    np.array([1,0.75,0.5,0.25,0.25,0.1,0.1])
  )

  # ejer3_convolucion(0.8,5)