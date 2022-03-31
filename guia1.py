import matplotlib.pyplot as plt
import numpy as np
from Signals import cuadrada, senoidal, sinc
from SignalsOperations import cuantizador, inversion, rectificacion
from interpolantes import interpolacion

def Ejer1 ():
    t1,y1 = senoidal(0,1,50)
    t2,y2 = sinc(-1,1,50,3,2)
    t3,y3 = cuadrada(0,1,50,2)
    fig, axs = plt.subplots(3,1)
    axs[0].stem(t1, y1)
    axs[1].stem(t2, y2)
    axs[2].stem(t3, y3)
    plt.show()

def Ejer2():
    t,y = senoidal(0,1,100,2)
    t1,y1 = inversion(t,y)
    y2 = rectificacion(y)
    y3 = cuantizador(y)
    fig,axs = plt.subplots(2,2)
    axs[0][0].stem(t,y)
    axs[0][1].stem(t1,y1)
    axs[1][0].stem(t,y2)
    axs[1][1].stem(t,y3)
    plt.show()

def Ejer3():
    # 0.01(s)/8(segmentos) -> 10*10*8 -> fm = 800Hz
    # Ts = 0.05s  -> fs = 1/Ts = 20Hz
    # phi' = 0.01-3*(0.01/8) = 0.00625
    # 2pi ~ 0.05 -> 0.00625 ~ -2*pi*0.00625/0.05
    # phi = -2*pi*0.00625/0.05
    # A = 3
    t,y = senoidal(0,0.1,800,20,-2*np.pi*0.00625/0.05)
    plt.stem(t,3*y)
    plt.show()
    pass

def Ejer4():
    fms = [100, 25, 10, 4, 1, 0.5]
    fig, axs = plt.subplots(2,3)
    i = 0; j = 0
    for fm in fms:
        t,y = senoidal(0,1,fm,5,0)
        axs[i][j].stem(t,y)
        axs[i][j].set_title('frecuencia de muestreo '+str(fm), fontsize=10)
        axs[i][j].set_xlabel('tiempo', fontsize=8)
        axs[i][j].set_ylabel('sinial', fontsize=8)
        axs[i][j].set_xlim(0,1)
        axs[i][j].set_ylim(-1,1)
        j += 1
        if j==3:
            i += 1; j = 0
    plt.show()

def Ejer5():
    t,y = senoidal(0,1,129,4000,0)
    plt.stem(t,y)
    plt.title('ejercicio 5')
    plt.xlabel('tiempo')
    plt.ylabel('senial')
    plt.show()

def Ejer6():
    t,y  = senoidal(0,1,10)
    ti,yi = interpolacion(t,y,40)
    fig, axs = plt.subplots(2,1)
    axs[0].stem(t,y)
    axs[0].set_xlim(0,1)
    axs[1].stem(ti,yi)
    axs[1].set_xlim(0,1)
    plt.show()

if __name__=='__main__':
    # Ejer1()
    # Ejer2()
    # Ejer3()
    # Ejer4()
    # Ejer5()
    Ejer6()