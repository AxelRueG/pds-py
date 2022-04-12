import numpy as np 
import matplotlib.pyplot as plt
from Signals import cuadrada, senoidal
from convolucion import convolucion_circular, convolucion_lineal

def ejer1 ():
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


if __name__ == '__main__':
  # respuesta_al_impulso(25, np.array([1]), np.array([-1]))
  # respuesta_al_impulso(25, np.array([1,0.5]), np.array([0]))
  # respuesta_al_impulso(25, np.array([1]), np.array([0.5,-0.25]))
  
  # CONVOLUCION ----------------------------------------------------------------
  yl = convolucion_lineal(np.array([0.5,1,1,0.5,0,-0.5,-1,-1,-0.5,0]),np.array([1,0.75,0.5,0.25,0.25,0.1,0.1]))
  yc = convolucion_circular(np.array([0.5,1,1,0.5,0,-0.5,-1,-1,-0.5,0]),np.array([1,0.75,0.5,0.25,0.25,0.1,0.1]))
  
  fig, ax = plt.subplots(2)
  fig.suptitle('convolucion lineal y circular')
  ax[0].stem(yl)
  ax[1].stem(yc)
  plt.show()