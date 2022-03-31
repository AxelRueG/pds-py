import numpy as np

def sinc(t):
    x = 2*np.pi*t*0.5
    index = np.nonzero(x != 0)
    y = np.ones(x.size)
    y[index] = np.sin(x[index])/x[index]
    return y
1
def interpolacion(t, x, fi):
    Ti = 1/fi
    T = t[1]-t[0]
    n = x.size
    m = (x.size*(fi*T)).astype(int)
    xi = np.zeros(m)
    for i in range(0,m):
        xi[i] = np.dot( x, sinc(((i*Ti)-(np.arange(0,n)*T))/T) )
    ti = np.arange(t[0],t[-1]+T,Ti)
    return ti,xi
