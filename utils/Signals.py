import numpy as np


def senoidal(t0, t1, fm, fs=1, phi=0, A=1):
    t = np.arange(t0, t1, 1/fm)
    y = A * np.sin(2*np.pi*t*fs+phi)
    return t, y


def sinc(t0, t1, fm, fs=1, phi=0):
    t = np.arange(t0, t1, 1/fm)
    x = 2*np.pi*t*fs + phi
    pos_zero = np.nonzero(x == 0)          # find index by x == 0
    y = np.sin(x)/x
    y[pos_zero] = 1
    return t, y


def cuadrada(t0, t1, fm, fs=1, phi=0):
    t = np.arange(t0, t1, 1/fm)
    x = np.mod(2*np.pi*fs*t+phi, 2*np.pi)
    positives = np.nonzero(x < np.pi)      # es un find index by x < pi
    y = np.ones(t.size)
    y[positives] = -1
    return t, y
