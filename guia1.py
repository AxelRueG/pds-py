import matplotlib.pyplot as plt
import numpy as np
from utils.Signals import cuadrada, senoidal, sinc
from utils.SignalsOperations import cuantizador, inversion, rectificacion_media_onda
from utils.interpolantes import escalon, interpolacion, lineal


def Ejer1():
    t1, y1 = senoidal(0, 1, 50)
    t2, y2 = sinc(-1, 1, 50, 3, 2)
    t3, y3 = cuadrada(0, 1, 50, 2)
    fig, axs = plt.subplots(3, 1)
    axs[0].stem(t1, y1)
    axs[1].stem(t2, y2)
    axs[2].stem(t3, y3)
    plt.show()


def Ejer2():
    t, y = senoidal(0, 1, 100, 2)
    t1, y1 = inversion(t, y)
    y2 = rectificacion_media_onda(y)
    y3 = cuantizador(y)
    fig, axs = plt.subplots(2, 2)
    axs[0][0].stem(t, y)
    axs[0][1].stem(t1, y1)
    axs[1][0].stem(t, y2)
    axs[1][1].stem(t, y3)
    plt.show()


def Ejer3():
    # 0.01(s)/8(segmentos) -> 10*10*8 -> fm = 800Hz

    # 0.05s es el tiempo en que ocurre un periodo
    # Ts = 0.05s  -> fs = 1/Ts = 20Hz

    # phi = -2 * pi * fs * (num_muetras_retardadas*fm) -> angulo de fase

    # A = 3

    # t0 tf fm fs phi
    phi = -2 * np.pi * 20 * (5 / 800)
    t, y = senoidal(0, 0.1, 800, 20, phi, 3)
    plt.stem(t, y)
    plt.show()
    pass


def Ejer4():
    fms = [100, 25, 10, 4, 1, 0.5]
    fig, axs = plt.subplots(2, 3)
    i = 0
    j = 0
    for fm in fms:
        t, y = senoidal(0, 1, fm, 5, 0)
        axs[i][j].stem(t, y)
        axs[i][j].set_title('frecuencia de muestreo '+str(fm), fontsize=10)
        axs[i][j].set_xlabel('tiempo', fontsize=8)
        axs[i][j].set_ylabel('sinial', fontsize=8)
        axs[i][j].set_xlim(0, 1)
        axs[i][j].set_ylim(-1, 1)
        j += 1
        if j == 3:
            i += 1
            j = 0
    plt.show()


def Ejer5():
    t, y = senoidal(0, 1, 129, 4000, 0)
    plt.stem(t, y)
    plt.title('ejercicio 5')
    plt.xlabel('tiempo')
    plt.ylabel('senial')
    plt.show()
    '''
    CONCLUSION: en la grafica podemos observar una senial con una frecuencia de 1Hz
    esto se debe a la baja frecuencia de muestreo, que coincidentemente en fm=129,
    muesta la senial antes descripta.
    para solucionarlo, deberiamos tener una fm al menos del doble de la fs 
    (para complir con el teorema del muestreo)
    '''


def Ejer6():
    t, y = senoidal(0, 1, 10)
    # func = [ sinc (default), lineal, escalon]
    ti, yi = interpolacion(t, y, 40, func=escalon)
    fig, axs = plt.subplots(2, 1)
    axs[0].stem(t, y)
    axs[0].set_xlim(0, 1)
    axs[1].stem(ti, yi)
    axs[1].set_xlim(0, 1)
    plt.show()


if __name__ == '__main__':
    # Ejer1()
    Ejer2()
    # Ejer3()
    # Ejer4()
    # Ejer5()
    # Ejer6()
