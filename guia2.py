import numpy as np 
import matplotlib.pyplot as plt

from Signals import cuadrada, senoidal
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

def delta_dirac(n, id=0):
  d = np.zeros(n)
  d[id] = 1
  return d

def respuesta_al_impulso(n, b, a):
  d = delta_dirac(n)
  print(d[0])
  y = np.zeros(n)
  p = b.size
  q = a.size
  for i in range(0,d.size):
    # np.arange(i,i-p,-1)
    # np.arange -> devuelve un rango entre a,b y un paso (en un intervalo cerrado abierto)
    # quiero que el rango vaya de i a i-p (donde p es la cantidad de entradas y salidas pasadas)
    y[i] = np.sum(b*d[np.arange(i,i-p,-1)])+np.sum(a*y[np.arange(i-1,i-q-1,-1)])

  plt.stem(y)
  plt.show()
  

if __name__ == '__main__':
  respuesta_al_impulso(25, np.array([1]), np.array([-1]))
  respuesta_al_impulso(25, np.array([1,0.5]), np.array([0]))
  respuesta_al_impulso(25, np.array([1]), np.array([0.5,-0.25]))
  