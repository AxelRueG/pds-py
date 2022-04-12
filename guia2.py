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
  

def convolucion_lineal(x,h):
  N = x.size+h.size-1
  y = np.zeros(N)
  x1 = np.append(x, np.zeros(h.size-1))
  h1 = np.append(h, np.zeros(x.size-1))
  for k in range(0,N):
    y[k] = sum(x1[0:N]*h1[k-np.arange(0,N)])

  return y

def convolucion_circular(x,h):
  N = h.size
  y = np.zeros(N)
  for k in range(0,N):
    # y[k] = np.dot(x1[k:k+N],h[h.size::-1])
    for l in range(0,N):
      print(l, '  ', (N+k-l)%N)
      y[k] += h[l]*x[((N+k-l)%N)]

  return y




if __name__ == '__main__':
  # respuesta_al_impulso(25, np.array([1]), np.array([-1]))
  # respuesta_al_impulso(25, np.array([1,0.5]), np.array([0]))
  # respuesta_al_impulso(25, np.array([1]), np.array([0.5,-0.25]))
  
  # y = convolucion_lineal(np.array([1,2,3,5,6]),np.array([1,0,0]))
  y = convolucion_circular(np.array([2,1,1.5,2,1.5,1]),np.array([3,2,1]))
  print(y)
  # plt.stem(y)
  # plt.show()