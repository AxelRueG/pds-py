import numpy as np

epsilon = 10**-9    # para el error numerico


def my_fft(s):
    N = s.shape[0]
    S = np.fft.fft(s)
    # pasamos la parte de las frecuencias negativas adelante
    S = np.concatenate((S[int((N)/2):], S[:int((N)/2)]))
    return S


def my_fft_f(s, fm):
    N = s.shape[0]
    S = np.fft.fft(s)
    # pasamos la parte de las frecuencias negativas adelante
    S = np.concatenate((S[int((N)/2):], S[:int((N)/2)]))
    f = np.arange(-fm/2, fm/2, fm/N)
    return f, S
