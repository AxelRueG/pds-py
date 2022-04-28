import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal

def parecido(fs,data):
  # rango de angulos de fase
  phis = np.arange(0, 2*np.pi, 0.1)
  parecido = -1000
  
  for i in range(0,phis.size):
    # medimos el parecido con el producto interno
    p = np.dot( senoidal(0,1,data.size,fs,phis[i])[1], data )
    if p>parecido: parecido=p

  return parecido

def calcular_frecuencias(data):
  filas = [697, 770, 852, 941]
  columnas = [1209, 1336, 1477]

  # buscamos la fila
  maxfil = -1000
  fil = -1
  for i in range(0,len(filas)):
    maxval = parecido(filas[i],data)
    if maxval>maxfil: 
      maxfil=maxval
      fil=i
  # buscamos la columna
  maxcol = -1000
  col = -1
  for i in range(0,len(columnas)):
    maxval = parecido(columnas[i],data)
    if maxval>maxcol: 
      maxcol=maxval
      col=i

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

  numero_discado = ''
  for numero in intervalos_de_numero:
    fil,col = calcular_frecuencias(data[numero[0]:numero[1]])
    numero_discado += teclado[fil][col]
  print(f'nuemero discado: {numero_discado}')
  

  # plt.plot(data)
  # plt.show()