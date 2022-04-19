import numpy as np

# ------------------------------------------------------------------------------
# n: longitud del vector
# i: "posicion" del indice 0 -> por ejemplo d[n-1] tendra en la posicion 1 el impulso unitario
def delta_dirac(n, i=0):
  d = np.zeros(n)
  d[i] = 1
  return d

# ------------------------------------------------------------------------------
# n: longitud del vector de salida
# a: coeficientes que multiplican a las entradas (i ... i-p)
# b: coeficientes que multiplican a las salidas (i-1 ... i-q)
def respuesta_al_impulso(n, a, b):
  # impulso unitario
  d = delta_dirac(n)
  
  y = np.zeros(n)
  p = a.size
  q = b.size
  for i in range(0,n):
    # np.arange(a,b,p) -> devuelve un vector entre a,b y un paso p (en un intervalo cerrado-abierto)
    # quiero que el rango vaya de i b i-p (donde p es la cantidad de entradas y salidas pasadas)
    y[i] = np.sum(a*d[range(i,i-p,-1)])+np.sum(b*y[range((i-1),(i-1)-q,-1)])

  # respuesta al impulso
  return y