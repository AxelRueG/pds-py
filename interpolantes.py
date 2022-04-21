from re import I
import numpy as np

from Signals import senoidal

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
        if 0<=t[i]<1:
            t0[i] = 1
    
    return t0

# ------------------------------------------------------------------------------
# t: tiempo de la senial
# x: valor de la senial
# fi: frecuencia interpolante
def interpolacion(t, x, fi, tipo=0):
    Ti = 1/fi            # periodo interpolante
    T = t[1]-t[0]        # periodo original
    n = x.size
    m = (x.size*(fi*T)).astype(int) # transformo en entero
    xi = np.zeros(m)
    for i in range(0,m):
        # interpolacion
        if tipo == 0:
            xi[i] = np.dot( x, sinc(((i*Ti)-(np.arange(0,n)*T))/T) )
        elif tipo == 1:
            xi[i] = np.dot( x, lineal(((i*Ti)-(np.arange(0,n)*T))/T) )
        else:
            xi[i] = np.dot( x, escalon(((i*Ti)-(np.arange(0,n)*T))/T) )
    # nuevos tiempos
    ti = np.arange(t[0],t[-1]+T,Ti)
    return ti,xi
