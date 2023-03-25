import numpy as np

# ------------------------------------------------------------------------------
def inversion(t,y):
    t1 = -1*t[t.size::-1]
    y1 = y[y.size::-1]
    return t1,y1

# ------------------------------------------------------------------------------
def rectificacion(y):
    y1 = y.copy()
    index = np.nonzero(y1<0)
    y1[index] = 0
    return y1

# ------------------------------------------------------------------------------
# x0: vector de entradas
# N:  niveles de cuantizacion
def cuantizador(x0,N=8):
    H = (2*x0.max())/N;
    xmin = x0.min()
    print(xmin)
    x = x0-xmin
    index = np.nonzero(x < (N-1)*H)
    x[index] = H*(x[index]/H).astype(int)
    x[np.nonzero(x >= (N-1)*H)] = (N-1)*H
    x += xmin
    return x
