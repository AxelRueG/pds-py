import numpy as np
import matplotlib.pyplot as plt
from utils.Signals import cuadrada, senoidal
from utils.convolucion import convolucion_circular, convolucion_lineal
from utils.sistemas import respuesta_al_impulso, delta_dirac
import scipy.signal as sgn

# EJERCICIO 1 - item 1 ---------------------------------------------------------


def ejer1_sistemas():
    # item 1
    fm = 50
    t, xn = cuadrada(0, 1, fm)
    w = 2*np.pi*2*np.arange(0, t.size)
    gn = 2*np.sin(w*1/fm)
    y = gn*xn

    fig, axs = plt.subplots(3, 1, constrained_layout=True)
    axs[0].stem(t, xn)
    axs[0].set_title('x[n]')
    axs[1].stem(t, gn)
    axs[1].set_title('g[n]')
    axs[2].stem(t, y)
    axs[2].set_title('y[n]')
    plt.show()

# EJERCICIO 4 ------------------------------------------------------------------


def ejer4_sistemas():
    y1 = respuesta_al_impulso(25, np.array([1]), np.array([0, 1]))
    y2 = respuesta_al_impulso(25, np.array([1, 0.5]), np.array([0]))
    y3 = respuesta_al_impulso(25, np.array([1]), np.array([0.5, -0.25]))

    # graficas
    fig, axs = plt.subplots(3, 1, constrained_layout=True)
    axs[0].stem(y1)
    axs[0].set_title('y[n]=x[n]+y[n-2]')
    axs[1].stem(y2)
    axs[1].set_title('y[n]=x[n]+0.5x[n-1]')
    axs[2].stem(y3)
    axs[2].set_title('y[n]=x[n]+0.5y[n-1]-0.25y[n-2]')
    plt.show()

# CONVOLUCION =================================================================
# convolucion lineal y circular comparadas


def ejer1y2_convolucion(x, h):
    yl = convolucion_lineal(x, h)
    y_conv = np.convolve(x, h)
    yc = convolucion_circular(x, h)

    # USANDO FILTER
    # completamos al de menor longitud con ceros
    cant = abs(x.size-h.size)
    x1 = x.copy() if (x.size > h.size) else np.concatenate((x, np.zeros(cant)))
    h1 = h.copy() if (x.size < h.size) else np.concatenate((h, np.zeros(cant)))
    A = delta_dirac(x1.size)
    y_fil = sgn.lfilter(h1, A, x1)

    fig, ax = plt.subplots(2, 2, constrained_layout=True)
    ax[0][0].stem(yl)
    ax[0][0].set_title('convolucion lineal')
    ax[0][1].stem(y_conv)
    ax[0][1].set_title('convolucion de python')
    ax[1][0].stem(yc)
    ax[1][0].set_title('convolucion circular')
    ax[1][1].stem(y_fil)
    ax[1][1].set_title('convolucion por filter')
    plt.show()

# EJERCICIO 3 ------------------------------------------------------------------


def ejer3_convolucion(a, N):
    n = np.arange(0, N)
    x = delta_dirac(N)-(a*delta_dirac(N, 1))
    ha = np.sin(8*n)
    hb = a**n

    # sistema en cascada
    y1 = convolucion_lineal(x, hb)
    y = convolucion_lineal(y1, ha)

    y2 = convolucion_lineal(x, ha)
    yw = convolucion_lineal(y2, hb)

    # resultados
    print(y.size)

    fig, ax = plt.subplots(2, constrained_layout=True)
    ax[0].stem(y)
    ax[0].set_title('y_conmutada[n]')
    ax[1].stem(yw)
    ax[1].set_title('y_normal[n]')
    plt.show()


# == MAIN =====================================================================
if __name__ == '__main__':
    # SISTEMAS -------------------------------------------------------------------
    # ejer1_sistemas()
    # ejer4_sistemas()
    # CONVOLUCION ----------------------------------------------------------------
    # ejer1y2_convolucion(
    #   np.array([1,2,2,0]),
    #   np.array([2,1,0.5,0])
    # )
    ejer1y2_convolucion(
        np.array([0.5, 1, 1, 0.5, 0, -0.5, -1, -1, -0.5, 0]),
        np.array([1, 0.75, 0.5, 0.25, 0.25, 0.1, 0.1])
    )

    # ejer3_convolucion(0.8,5)
