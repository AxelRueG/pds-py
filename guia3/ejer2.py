import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils.Signals import senoidal


def producto_interno(s1, s2): return np.dot(s1, s2)

'''
NOTA: me he dado cuenta, que en lo particular con una senial senosoidal,
el valor del producto punto de un vector con sigo mismo es igual a la mitad de 
la frecuencia de muestreo
'''
# ------------------------------------------------------------------------------
# variacion: tipo de variacion en la senial a comparat ['phi','fs','ambos']
def ejer_2(variacion='ambos'):
    fm = 64
    t, ya = senoidal(0, 1, fm, 2)

    # funcion que produce la animacion
    def comparacion_animada(val):
        _, y = senoidal(0, 1, fm, val[0], val[1])
        ax.clear()
        ax.plot(t, ya)
        ax.stem(t, y)
        ax.set_xlim(0, 1)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xlabel('tiempo [s]')
        ax.set_ylabel('x[n]')
        plt.title(f'parecido <u,v>: {round(producto_interno(ya,y),2)}')
        plt.show()

    # datos de la animacion
    phis = np.arange(0, 2*np.pi, 0.1)
    frecuencias = np.linspace(1, 4, phis.size)

    # animacion
    fig, ax = plt.subplots()

    if variacion == 'fs':
        # variacion de frecuencias
        frames2 = np.transpose(np.array([frecuencias, np.zeros(phis.size)]))
        animate = FuncAnimation(
            fig, func=comparacion_animada, frames=frames2, interval=10)
    elif variacion == 'phi':
        # variacion de phi
        frames1 = np.transpose(np.array([np.ones(phis.size)+1, phis]))
        animate = FuncAnimation(
            fig, func=comparacion_animada, frames=frames1, interval=10)
    else:
        # variacion de ambos
        frames3 = np.transpose(np.array([frecuencias, phis]))
        animate = FuncAnimation(
            fig, func=comparacion_animada, frames=frames3, interval=10)

    plt.show()
