import numpy as np

def sinc(t):
    x = 2*np.pi*t*0.5
    index = np.nonzero(x != 0)
    y = np.ones(x.size)
    y[index] = np.sin(x[index])/x[index]
    return y

# ------------------------------------------------------------------------------
# t: tiempo de la senial
# x: valor de la senial
# fi: frecuencia interpolante
def interpolacion(t, x, fi):
    Ti = 1/fi            # periodo interpolante
    T = t[1]-t[0]        # periodo original
    n = x.size
    m = (x.size*(fi*T)).astype(int) # transformo en entero
    xi = np.zeros(m)
    for i in range(0,m):
        # interpolacion
        xi[i] = np.dot( x, sinc(((i*Ti)-(np.arange(0,n)*T))/T) )
    # nuevos tiempos
    ti = np.arange(t[0],t[-1]+T,Ti)
    return ti,xi
