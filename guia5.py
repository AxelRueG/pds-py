from matplotlib import pyplot as plt
import numpy as np

from sistemas import delta_dirac

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
  # fun_a = lambda z: sum((2**-k)(z**-k))

  # datos
  fm = 10000
  z = np.arange(0,1,1/fm)*(2*np.pi)
  N = z.shape[0]

  # calculo la  respuesta en frecuencias
  Hk = fun_a(np.exp(1j*z))  # estamos evaluando H(z) en z=re^(jwn)
  hn_calc = np.fft.ifft(Hk)

  hn = fa(delta_dirac(fm))
  Hk_calc = np.fft.fft(hn)
  # Hk_calc = np.concatenate((Hk_calc[int((N)/2):], Hk_calc[:int((N)/2)]))

  ## invertimos las frecuencias negativas
  # f = np.arange(-fm/2,fm/2,fm/N)

  # GRAFICAS 
  fig,ax = plt.subplots(2,2)
  ax[0][0].plot(hn)
  ax[0][0].set_title('respuesta al impulso')
  ax[0][1].plot(abs(Hk_calc))
  ax[0][1].set_title('respuesta en frecuencia calculada')
  ax[1][0].plot(np.real(hn_calc))
  ax[1][0].set_title('respusta al impulso resultado de Hz')
  ax[1][1].plot(abs(Hk))
  ax[1][1].set_title('respuesta en frecuencia form')
  plt.show()

if __name__=='__main__':
  ejer_2()