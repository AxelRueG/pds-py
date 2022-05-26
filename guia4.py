import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal


'''
NOTAS:
0 - en la transformada de la senial original, tenemos los picos en las frecuencias de las senoidales puras que la conforman (10 y 20) donde f2 tiene 4 veces mas amplitud que f1 como se denota en la formula de la senial.
1 - en la senial a la que sumamos 4 notamos que aparece un pico en f=0, ya que le sumamos una constante con frecuencia 0 ya que no se repite ningun ciclo y esta continua hasta el infinito. 
3 - supongo que al calcular delta_f=fm/N dando 1 (al ser N=1000 y fm=1000) solo tenemos frecuencias "enteras", por lo cual al tener f2=10.5 no la reconoce y la distribuye entre frecuencias cercanas a la que buscamos
4 - en este caso la frecuencia f2=10.5 esta bien remarcada ya que al aumentar la duracion de la senial a 2seg, aumentamos al doble el numero de muestras, lo que nos da como resultado 1000/2000=0.5 al calcular el delta_f 
'''
def ejer1():
  tf = 1       # tiempo final del intervalo
  f1 = 10
  f2 = 20      # opciones: [20, 11, 10.5]
  fm = 1000
  t = np.arange(0,tf,1/fm)
  s = senoidal(0,tf,fm,f1)[1]+(4*senoidal(0,tf,fm,f2)[1])
  # s = senoidal(0,tf,fm,f1)[1]+(4*senoidal(0,tf,fm,f2)[1])+4
  
  N = s.shape[0]
  S = np.fft.fft(s)
  # pasamos la parte de las frecuencias negativas adelante
  S = np.concatenate((S[int((N)/2):], S[:int((N)/2)]))
  df = fm/2
  f = np.arange(-df,df,fm/N)  # rango de la transformada de fourier

  # condicion de perceval
  epsilon = 10**-6    # para el error numerico
  perseval1 = sum(s**2)
  perseval2 = (1/N)*sum(abs(S)**2)
  if abs(perseval1-perseval2) < epsilon:
    print('son iguales')
  else:
    print('son distintos')

  # plots
  fig,ax = plt.subplots(2,1)
  ax[0].plot(t,s)
  ax[1].stem(f,abs(S))
  plt.show()

if __name__=="__main__":
  ejer1()