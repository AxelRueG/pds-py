import numpy as np
from pandas import Interval
import scipy.linalg as scl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Signals import senoidal

def signal_info(x):
  pm = sum(x**2)/x.size
  print('valor medio:', np.mean(x))
  print('maximo:', np.max(x))
  print('minimo:', np.min(x))
  print('amplitud:', scl.norm(x,np.inf))
  print('energia:', scl.norm(x))
  print('accion:', scl.norm(x,1))
  print('potencia media:', pm)
  print('raiz del valor cuadratico medio:', np.sqrt(pm))

def ejer_1 (n):
  y = np.random.randint(-10,10,size=n)/10      # senial aleatorea de [-1:1] 
  signal_info(y)
  plt.stem(y)
  plt.show()

producto_interno = lambda s1,s2: np.dot(s1,s2)


def ejer_2():
  t, ya = senoidal(0,1,50,2)
  # funcion que produce la animacion
  def comparacion_animada(val):
    _, y  = senoidal(0,1,50,val[0],val[1])
    ax.clear()
    ax.plot(t,ya)
    ax.stem(t,y)
    ax.set_xlim(0,1)
    ax.set_ylim(-1.5,1.5)
    plt.title(f'parecido <u,v>: {round(producto_interno(ya,y),2)}')
    plt.show()

  # datos de la animacion
  phis = np.arange(0,2*np.pi,0.1)
  frecuencias = np.linspace(1,4,phis.size)

  # animacion
  fig, ax = plt.subplots()

  ## variacion de phi
  frames1 = np.transpose(np.array([ np.ones(phis.size)+1, phis ]))
  animate = FuncAnimation(fig,func=comparacion_animada,frames=frames1, interval=10)

  ## variacion de frecuencias
  # frames2 = np.transpose(np.array([ frecuencias, np.zeros(phis.size) ]))
  # animate = FuncAnimation(fig,func=comparacion_animada,frames=frames2, interval=10)

  ## variacion de ambos
  # frames3 = np.transpose(np.array([ frecuencias, phis ]))
  # animate = FuncAnimation(fig,func=comparacion_animada,frames=frames3, interval=10)
  plt.show()

if __name__ == '__main__':
  ejer_2()