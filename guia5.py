from matplotlib import pyplot as plt
import numpy as np

from sistemas import respuesta_al_impulso
from zplane import zplane

'''
-- EJERCICIO 1 -----------------------------------------------------------------
- Item a
  y[n]-1/2y[n-1]+1/4y[n-2] = x[n]
  Y(z)-1/2Y(z)(z^-1)+1/4Y(z)(z^-2) = X(z)
  Y(z)*[1-1/2(z^-1)+1/4(z^-2)] = X(z)
  H(z) = Y(z)/X(z) = 1/(1-1/2(z^-1)+1/4(z^-2))

- Item b
  y[n] = y[n-1]+y[n-2]+x[n-1]
  y[n]-y[n-1]-y[n-2] = x[n-1]
  Y(z)-Y(z)(z^-1)-Y(z)(z^-2) = X(z)(z^-1)
  Y(z)(1-(z^-1)-(z^-2)) = X(z)(z^-1)
  H(z) = Y(z)/X(z) = (z^-1)/(1-(z^-1)-(z^-2))

- Item c
  y[n] = 7x[n]+2y[n-1]-6y[n-2]
  y[n]-2y[n-1]+6y[n-2] = 7x[n]
  Y(z)-2Y(z)(z^-1)+6Y(z)(z^-2) = 7X(z)
  Y(z)(1-2(z^-1)+6(z^-2)) = 7X(z)
  H(z) = Y(z)/X(z) = 7/(1-2(z^-1)+6(z^-2))

- Item d
  y[n] = sum((2^-k)x[n-k])|k=[0,7]
  Y(z) = sum((2^-k)X(z)(z^-k))|k=[0,7]               # tranzformada en z
  Y(z) = X(z)*sum((2^-k)(z^-k))|k=[0,7]              # saco X(z) de la sumatoria
  H(z) = Y(z)/X(z) = sum((2^-k)(z^-k))|k=[0,7]       # funcion de transferencia
'''

def fa(x):
  y = np.zeros(x.shape[0])
  for n in range(x.shape[0]):
    y[n] = x[n]+0.5*y[n-1]-0.25*y[n-2]
  return y

def ejer_2():
  # FUNCIONES
  fun_a = lambda z: 1/(1-0.5*(z**-1)+0.25*(z**-2))
  fun_b = lambda z: (z**-1)/(1-(z**-1)-(z**-2))
  fun_c = lambda z: 7/(1-2*(z**-1)+6*(z**-2))
  def fun_d(z):
    zd = np.zeros(z.shape[0])
    for k in range(8): zd = zd+((2**-k)*(z**-k))
    return zd

  # datos
  fm = 10000
  z = np.arange(0,1,1/fm)*(2*np.pi)
  N = z.shape[0]

  # calculo la  respuesta en frecuencias
  Hk = fun_d(np.exp(1j*z))  # estamos evaluando H(z) en z=re^(jwn)
  hn_calc = np.fft.ifft(Hk)

  ## invertimos las frecuencias negativas y calcular frecuencias
  Hk = np.concatenate((Hk[int((N)/2):], Hk[:int((N)/2)]))
  f = np.arange(-fm/2,fm/2,fm/N)

  # GRAFICAS
  fig,ax = plt.subplots(2,constrained_layout=True)
  ax[0].plot(f,abs(Hk))
  ax[0].set_title('respuesta en frecuencia')
  ax[0].set_xlabel('frecuencias')
  ax[0].set_ylabel('H[k]')
  ax[1].stem(np.real(hn_calc))
  ax[1].set_title('respusta al impulso')
  ax[1].set_xlabel('n')
  ax[1].set_ylabel('h[n]')
  plt.show()

def ejer_3():
  '''
  tenemos:
  H(z) = (1-2z^-1+2z^-2-z^-3)/((1-z^-1)(1-0.5z^-1)(1-0.2z^-1))
  Y(z)/X(z) = (1-2z^-1+2z^-2-z^-3)/((1-z^-1)(1-0.5z^-1)(1-0.2z^-1))
  Y(z)((1-z^-1)(1-0.5z^-1)(1-0.2z^-1)) = X(z)(1-2z^-1+2z^-2-z^-3)
  Y(z)(1-1.7(z^-1)+0.8(z^-2)-0.1(z^-3)) = X(z)(1-2z^-1+2z^-2-z^-3)
  Y(z)-1.7Y(z)(z^-1)+0.8Y(z)(z^-2)-0.1Y(z)(z^-3) = X(z)-2X(z)(z^-1)+2X(z)(z^-2)-X(z)(z^-3)
  y[n]-1.7y[n-1]+0.8y[n-2]-0.1y[n-3] = x[n]-2x[n-1]+2x[n-2]-x[n-3]
  '''
  h = respuesta_al_impulso(100,
      np.array([1,-2,2,-1]),
      np.array([1.7,-0.8,0.1]))
      
  '''
  NOTA: segun el analicis de polos y ceros, podemos determinar que el sistema es estable,
  como podemos apreciar en la grafica de la respusta al impulso, que es finita.
  '''
  zplane(np.array([1,-2,2,-1]),np.array([1,-1.7,0.8,-0.1]))

  # GRAFICAS 
  fig,ax = plt.subplots()
  ax.stem(h)
  ax.set_title('respuesta al impulso')
  ax.set_xlabel('n')
  ax.set_ylabel('h[n]')

  plt.show()

if __name__=='__main__':
  # ejer_2()
  ejer_3()