import numpy as np

# ------------------------------------------------------------------------------
# x: vector de entradas
# h: respuesta al impulso
def convolucion_lineal(x,h):
  # longitud de la salida (tener en cuenta como se multiplican)
  N = x.size+h.size-1 
  y = np.zeros(N)
  # agregamos ceros a los vectores de entrada y respuesta
  x1 = np.append(x, np.zeros(h.size-1))
  h1 = np.append(h, np.zeros(x.size-1))

  for k in range(0,N):
    # no nos importa los indices negativos, son ceros
    y[k] = sum(x1[0:N]*h1[k-np.arange(0,N)])

  return y

# ------------------------------------------------------------------------------
# x: vector de entradas
# h: respuesta al impulso
def convolucion_circular(xn,hn):
  N = max(xn.size,hn.size)

  # entrada x[n] ciclica
  x = xn.copy()
  while (x.size < N):
    x = np.concatenate(( x, x[0:N-x.size] ))

  h = hn.copy()
  while (h.size < N):
    h = np.concatenate(( h, h[0:N-h.size] ))

  y = np.zeros(N)  
  # convolucion
  for k in range(0,N):
    for l in range(0,N):
      y[k] += h[l]*x[(N+k-l)%N]

  return y
