from re import I
import numpy as np

def sinc(t):
    x = 2*np.pi*t*0.5
    index = np.nonzero(x != 0)
    y = np.ones(x.size)
    y[index] = np.sin(x[index])/x[index]
    return y

def lineal (t):
    return 1-np.abs(t)

def escalon (t):
    t0 = np.zeros(t.size)
    for i in range(0,t.size):
        if 0<=t[i]<1: t0[i] = 1
    return t0

# ------------------------------------------------------------------------------
# t: tiempo de la senial
# x: valor de la senial
# fi: frecuencia interpolante
# func: funcion interpolante
def interpolacion(t, x, fi, func=sinc):
    Ti = 1/fi            # periodo interpolante
    T = t[1]-t[0]        # periodo original
    n = x.size
    m = (x.size*(fi*T)).astype(int) # transformo en entero
    xi = np.zeros(m)
    for i in range(0,m):
        # interpolacion
        xi[i] = np.dot( x, func((i*Ti/T)-np.arange(0,n)) )
    # nuevos tiempos
    ti = np.arange(t[0],t[-1]+T,Ti)
    return ti,xi
