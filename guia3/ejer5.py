import numpy as np
from Signals import senoidal

import time

def senial_desfasada(fs,data):
  # rango de angulos de fase
  phis = np.arange(0, 2*np.pi, 0.1)
  parecido = -1000
  # comparamos con una frecuencia desfasada
  for i in range(0,phis.size):
    # medimos el parecido
    p = np.dot( senoidal(0,1,data.size,fs,phis[i])[1], data )
    if p>parecido: parecido=p    # nos quedamos con el maximo parecido
  return parecido

def mas_parecido(fs,data):
  maxfil = -1000
  indice = -1
  # vamos recorreindo las frecuencias de la fila o columna
  for key in range(0,len(fs)):
    parecido = senial_desfasada(fs[key],data)
    # comparamos cual frecuencia se parece mas a la de data
    if parecido>maxfil: 
      maxfil=parecido
      indice=key

  return indice

def calcular_frecuencias(data):
  filas = [697, 770, 852, 941]
  columnas = [1209, 1336, 1477]

  fil = mas_parecido(filas,data)
  col = mas_parecido(columnas,data) 

  return fil, col


def ejer_5():
  data = np.loadtxt('/home/axel/Documents/fich/PDS/src/datasets/te.txt')

  # Intervalos de cada numero discado
  intervalos_de_numero = [[ 17200,  21800 ],
                          [ 30000,  35000 ],
                          [ 39700,  43600 ],
                          [ 48200,  53300 ],
                          [ 59000,  63500 ],
                          [ 69800,  74600 ],
                          [ 80500,  85500 ]]
  # teclado numerico
  teclado = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9'],
             ['*','0','#']]

  ini = time.time()
  
  numero_discado = ''
  for numero in intervalos_de_numero:
    fil,col = calcular_frecuencias(data[numero[0]:numero[1]])
    numero_discado += teclado[fil][col]
  print(f'nuemero discado: {numero_discado}')
  
  fin = time.time()
  print(f'tiempo: {fin-ini}seg')
