import numpy as np
from Signals import senoidal, cuadrada
from guia4.fft import my_fft,epsilon

def ejer2(inciso=0):
  # definimos el producto interno
  producto_interno = lambda a,b: np.dot(a,np.conj(b)) 

  # datos de entrada
  t0 = 0
  t1 = 1
  fm = 100
  # seniales 
  sn = ['a','b','c']
  s = np.array([senoidal(t0,t1,fm,2)[1],cuadrada(t0,t1,fm,2)[1],senoidal(t0,t1,fm,4)[1]])
  if inciso:
    sn = ['a','c']
    s = np.array([senoidal(t0,t1,fm,2)[1],senoidal(t0,t1,fm,3.5)[1]])

  p = 0
  while p<len(s):
    q = (p+1)%len(s)
    print(f'-- comparativa senial {sn[p]} y {sn[q]} -----------------------')
    ortogonalidad = producto_interno(s[p],s[q])
    if (ortogonalidad<epsilon):
      print('son ortogonales en el dominio temporal')
    else:
      print('no son ortogonales en el dominio temporal')

    S1 = my_fft(s[p])
    S2 = my_fft(s[q])
    ortogonalidad_trasnformada = producto_interno(S1,S2)
    if (ortogonalidad_trasnformada<epsilon):
      print('son ortogonales en el dominio frecuencial')
    else:
      print('no son ortogonales en el dominio frecuencial')

    p+=1