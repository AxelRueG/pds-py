import numpy as np
import matplotlib.pyplot as plt
from guia4.fft import my_fft,epsilon
from Signals import senoidal

'''
NOTAS:
0 - en la transformada de la senial original, tenemos los picos en las frecuencias de las senoidales puras que la conforman (10 y 20) donde f2 tiene 4 veces mas amplitud que f1 como se denota en la formula de la senial. Tambien podemos obserbar que la amplitud de f1 es fm/2 y la amplitud de f2 es de 4fm/2
en el dominio de la frecuencia
1 - en la senial a la que sumamos 4 notamos que aparece un pico en f=0, ya que le sumamos una constante con frecuencia 0 ya que no se repite ningun ciclo y esta continua hasta el infinito. 
3 - supongo que al calcular delta_f=fm/N dando 1 (al ser N=1000 y fm=1000) solo tenemos frecuencias "enteras", por lo cual al tener f2=10.5 no la reconoce y la distribuye entre frecuencias cercanas a la que buscamos
4 - en este caso la frecuencia f2=10.5 esta bien remarcada ya que al aumentar la duracion de la senial a 2seg, aumentamos al doble el numero de muestras, lo que nos da como resultado 1000/2000=0.5 al calcular el delta_f 
'''
def ejer1(ti=0,tf=1,f1=10,f2=20,fm=1000):
  
  t = np.arange(ti,tf,1/fm)
  # s = senoidal(ti,tf,fm,f1)[1]+(4*senoidal(ti,tf,fm,f2)[1])
  s = senoidal(0,tf,fm,f1)[1]+(4*senoidal(0,tf,fm,f2)[1])+4
  
  N = s.shape[0]
  S = my_fft(s)
  df = fm/2
  f = np.arange(-df,df,fm/N)  # rango de la transformada de fourier

  # condicion de parceval
  parseval1 = sum(s**2)
  parseval2 = (1/N)*sum(abs(S)**2)
  if abs(parseval1-parseval2) < epsilon:
    print('son iguales')
  else:
    print('son distintos')

  # -- GRAFICOS ----------------------------------------------------------------
  fig,ax = plt.subplots(2,1,constrained_layout=True)
  ax[0].stem(t,s)
  ax[0].set_title('senial')
  ax[0].set_xlabel('tiempo [s]')
  ax[0].set_ylabel('x[n]')
  ax[1].stem(f,abs(S))
  ax[1].set_title('transformada')
  ax[1].set_xlabel('frecuencias [Hz]')
  ax[1].set_ylabel('|X[k]|')
  plt.show()
