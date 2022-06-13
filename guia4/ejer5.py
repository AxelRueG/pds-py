import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal
from guia4.fft import my_fft_f


'''
NOTAS:
en la senial podemos observar una frecuencia de (mas menos) 23 hrz
podemos observar que como el dominio en el espacio de las frecuencias va de [-fm/2:fm/2)
podemos ver representada hasta (fm/2)-1 Hz. al pasarnos de ese numero una frecuencia distinta
en el intervalo sera representada, dada por la formula que describimos mas abajo

'''
def ejer5(fm=50,fs=27):
  ecuacion_b = lambda fm,fs: (((fs//(fm/2))+1)%2)*(fs%(fm/2))+((fs//(fm/2))%2)*((fm-fs)%(fm/2))
  print(f'la frecuencia real es: {fs} pero la que vemos en la ttf es {ecuacion_b(fm,fs)}')

  ## 2*sin(2*pi*fs*t)
  t,x = senoidal(0,1,fm,fs)
  x*=2
  f,X = my_fft_f(x,fm)

  # -- GRAFICOS ----------------------------------------------------------------
  ## graficos de la senial muestreada
  fig,ax = plt.subplots(2,constrained_layout=True)
  ax[0].stem(t,x)
  ax[0].set_title('senial muestreada')
  ax[0].set_xlabel('tiempo [s]')
  ax[0].set_ylabel('x[t]')
  ax[1].stem(f,abs(X))
  ax[1].set_title('transformada de fourier')
  ax[1].set_xlabel('frecuencias [hz]')
  ax[1].set_ylabel('abs(X[k])')

  ## frecuencias percividas en la transformada de fourier
  fig,ax1 = plt.subplots()
  ax1.stem(ecuacion_b(50,np.arange(0,106)))
  ax1.set_title('frecuencias percividas por mal muestreo')
  ax1.set_xlabel('frecuencia real [hz] ')
  ax1.set_ylabel('frecuencia percibida [hz]')

  plt.show()