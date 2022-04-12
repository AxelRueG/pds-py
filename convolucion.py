import numpy as np

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

  return y
  

def convolucion_lineal(x,h):
  N = x.size+h.size-1 
  y = np.zeros(N)
  x1 = np.append(x, np.zeros(h.size-1))
  h1 = np.append(h, np.zeros(x.size-1))

  for k in range(0,N):
    y[k] = sum(x1[0:N]*h1[k-np.arange(0,N)])

  return y


def convolucion_circular(xn,hn):
  N = max(xn.size,hn.size)

  # entrada x[n] ciclica -------------------------------------------------------
  x = xn.copy()
  while (x.size < N):
    x = np.hstack(( x, x[0:N-x.size] ))

  # en caso de la respuesta al impulso completada con ceros --------------------
  h = np.hstack((hn, np.zeros(N-hn.size) ))

  y = np.zeros(N)  
  # convolucion con ciclos for -------------------------------------------------
  for k in range(0,N):
    for l in range(0,N):
      y[k] += h[l]*x[(N+k-l)%N]

  return y
