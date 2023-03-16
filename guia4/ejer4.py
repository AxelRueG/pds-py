import numpy as np
import matplotlib.pyplot as plt
from guia4.fft import my_fft, my_fft_f


def width_ventana(window_func, L, porcentaje):
    N = int(porcentaje*L)
    ns = int((L-N)/2)
    resto = (L-N) % 2
    s = np.zeros(L)
    s[ns+resto:L-ns] = window_func(N)
    return s


def ejer4(window_func, window_name):
    L = 500

    s1 = width_ventana(window_func, L, 0.2)
    s2 = width_ventana(window_func, L, 0.5)
    s3 = width_ventana(window_func, L, 0.8)

    S1 = my_fft(s1)
    S2 = my_fft(s2)
    S3 = my_fft(s3)
    # GRAFICAS
    fig, ax = plt.subplots(3, 2, constrained_layout=True)
    ax[0][0].plot(s1)
    ax[0][0].set_title(f'ventana {window_name} fina')
    ax[0][0].set_xlabel('n')
    ax[0][0].set_ylabel('x[n]')
    ax[1][0].plot(s2)
    ax[1][0].set_title(f'ventana {window_name} media')
    ax[1][0].set_xlabel('n')
    ax[1][0].set_ylabel('x[n]')
    ax[2][0].plot(s3)
    ax[2][0].set_title(f'ventana {window_name} ancha')
    ax[2][0].set_xlabel('n')
    ax[2][0].set_ylabel('x[n]')
    ax[0][1].plot(abs(S1))
    ax[0][1].set_title('transformada de fourier')
    ax[0][1].set_xlabel('frecuencia [Hz]')
    ax[0][1].set_ylabel('X[k]')
    ax[1][1].plot(abs(S2))
    ax[1][1].set_title('transformada de fourier')
    ax[1][1].set_xlabel('frecuencia [Hz]')
    ax[1][1].set_ylabel('X[k]')
    ax[2][1].plot(abs(S3))
    ax[2][1].set_title('transformada de fourier')
    ax[2][1].set_xlabel('frecuencia [Hz]')
    ax[2][1].set_ylabel('X[k]')
    plt.show()
