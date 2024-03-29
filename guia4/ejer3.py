import numpy as np
import matplotlib.pyplot as plt
from utils.Signals import senoidal


def ejer3(fs=10, fm=100, despazamiento=10):

    t = np.arange(0, 1, 1/fm)
    s = senoidal(0, 1, fm, 10)[1]
    S = np.fft.fft(s)
    N = S.shape[0]
    f = np.arange(-fm/2, fm/2, fm/N)

    S_desfasado = S*np.exp((-1j*2*np.pi*np.arange(N)*despazamiento)/N)
    s_desfasado = np.fft.ifft(S_desfasado)

    S = np.concatenate((S[int((N)/2):], S[:int((N)/2)]))
    S_desfasado = np.concatenate((S_desfasado[int((N)/2):], S_desfasado[:int((N)/2)]))

    # -- GRAFICAS ----------------------------------------------------------------
    fig, ax = plt.subplots(2, 2, constrained_layout=True)
    ax[0][0].stem(t, s)
    ax[0][0].set_title('senoidal')
    ax[0][0].set_xlabel('tiempo [s]')
    ax[0][0].set_ylabel('x[n]')
    ax[1][0].stem(f, abs(S))
    ax[1][0].set_title('senoidal transformada')
    ax[1][0].set_xlabel('frecuencia [Hz]')
    ax[1][0].set_ylabel('|X[k]|')
    ax[0][1].stem(f, abs(S_desfasado))
    ax[0][1].set_title('senoidal transformada desplazada')
    ax[0][1].set_xlabel('frecuencia [Hz]')
    ax[0][1].set_ylabel('|X[k]|')
    # s_desfasado posee parte imaginaria
    ax[1][1].stem(t, np.real(s_desfasado))
    ax[1][1].set_title('senoidal despazada')
    ax[1][1].set_xlabel('tiempo [s]')
    ax[1][1].set_ylabel('x[n]')
    plt.show()
