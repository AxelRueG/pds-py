import numpy as np

# ------------------------------------------------------------------------------
def inversion(t,y):
    t1 = -1*t[t.size::-1]
    y1 = y[y.size::-1]
    return t1,y1

# ------------------------------------------------------------------------------
def rectificacion_media_onda(y):
    y1 = y.copy()
    index = np.nonzero(y1<0)
    y1[index] = 0
    return y1

# ------------------------------------------------------------------------------
def rectificacion_onda_completa(y):
    return abs(y)

# ------------------------------------------------------------------------------
# x0: vector de entradas
# N:  niveles de cuantizacion
def cuantizador(x0,N=8):
    # H = (2*x0.max())/N
    H = round(x0.max()-x0.min())/N
    xmin = x0.min()
    x = x0-xmin
    index = np.nonzero(x < (N-1)*H)
    x[index] = H*(x[index]/H).astype(int)
    x[np.nonzero(x >= (N-1)*H)] = (N-1)*H
    # for i in range(x.shape[0]):
    #     if(x[i]<0):
    #         x[i]=0
    #     elif 0 <= x[i] < (N-1)*H:
    #         x[i]=H*round(x[i]/H);
    #     else:
    #         x[i]=(N-1)*H;
    return x+xmin
