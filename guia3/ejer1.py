import numpy as np
import scipy.linalg as scl
import matplotlib.pyplot as plt

from utils.Signals import senoidal


def signal_info(x):
    pm = sum(x**2)/x.size
    print('valor medio:', np.mean(x))
    print('maximo:', np.max(x))
    print('minimo:', np.min(x))
    print('amplitud:', scl.norm(x, np.inf))
    print('energia:', scl.norm(x))
    print('accion:', scl.norm(x, 1))
    print('potencia media:', pm)
    print('raiz del valor cuadratico medio:', np.sqrt(pm))


def ejer_1(n):
    y = (2*np.random.rand(n))-1      # senial aleatorea de [-1:1]
    # y1 = senoidal(0,1,n,2)      # senial aleatorea de [-1:1]
    signal_info(y)
    # signal_info(y1)
    plt.stem(y)
    plt.show()
