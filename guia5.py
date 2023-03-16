from matplotlib import pyplot as plt
import numpy as np

from utils.sistemas import respuesta_al_impulso
from utils.zplane import zplane

'''
-- EJERCICIO 1 -----------------------------------------------------------------
- Item a
  y[n]-1/2y[n-1]+1/4y[n-2] = x[n]
  Y(z)-1/2Y(z)(z^-1)+1/4Y(z)(z^-2) = X(z)
  Y(z)*[1-1/2(z^-1)+1/4(z^-2)] = X(z)
  H(z) = Y(z)/X(z) = 1/(1-1/2(z^-1)+1/4(z^-2))

- Item b
  y[n] = y[n-1]+y[n-2]+x[n-1]
  y[n]-y[n-1]-y[n-2] = x[n-1]
  Y(z)-Y(z)(z^-1)-Y(z)(z^-2) = X(z)(z^-1)
  Y(z)(1-(z^-1)-(z^-2)) = X(z)(z^-1)
  H(z) = Y(z)/X(z) = (z^-1)/(1-(z^-1)-(z^-2))

- Item c
  y[n] = 7x[n]+2y[n-1]-6y[n-2]
  y[n]-2y[n-1]+6y[n-2] = 7x[n]
  Y(z)-2Y(z)(z^-1)+6Y(z)(z^-2) = 7X(z)
  Y(z)(1-2(z^-1)+6(z^-2)) = 7X(z)
  H(z) = Y(z)/X(z) = 7/(1-2(z^-1)+6(z^-2))

- Item d
  y[n] = sum((2^-k)x[n-k])|k=[0,7]
  Y(z) = sum((2^-k)X(z)(z^-k))|k=[0,7]               # tranzformada en z
  Y(z) = X(z)*sum((2^-k)(z^-k))|k=[0,7]              # saco X(z) de la sumatoria
  H(z) = Y(z)/X(z) = sum((2^-k)(z^-k))|k=[0,7]       # funcion de transferencia
'''

# funciones ejer 2 -------------------------------------------------------------
def fun_item_a(z): return 1/(1-0.5*(z**-1)+0.25*(z**-2))
def fun_item_b(z): return (z**-1)/(1-(z**-1)-(z**-2))
def fun_item_c(z): return 7/(1-2*(z**-1)+6*(z**-2))

def fun_item_d(z):
    zd = np.zeros(z.shape[0])
    for k in range(8):
        zd = zd+((2**-k)*(z**-k))
    return zd


def ejer_2(fun):
    # datos
    fm = 10000
    z = np.arange(0, 1, 1/fm)*(2*np.pi)
    N = z.shape[0]

    # calculo la  respuesta en frecuencias
    Hk = fun(np.exp(1j*z))  # estamos evaluando H(z) en z=re^(jwn)
    hn_calc = np.fft.ifft(Hk)

    # invertimos las frecuencias negativas y calcular frecuencias
    Hk = np.concatenate((Hk[int((N)/2):], Hk[:int((N)/2)]))
    f = np.arange(-fm/2, fm/2, fm/N)

    # GRAFICAS
    fig, ax = plt.subplots(2, constrained_layout=True)
    ax[0].plot(f, abs(Hk))
    ax[0].set_title('respuesta en frecuencia')
    ax[0].set_xlabel('frecuencias')
    ax[0].set_ylabel('H[k]')
    ax[1].stem(np.real(hn_calc))
    ax[1].set_title('respusta al impulso')
    ax[1].set_xlabel('n')
    ax[1].set_ylabel('h[n]')
    plt.show()


def ejer_3():
    '''
    tenemos:
    H(z) = (1-2z^-1+2z^-2-z^-3)/((1-z^-1)(1-0.5z^-1)(1-0.2z^-1))
    Y(z)/X(z) = (1-2z^-1+2z^-2-z^-3)/((1-z^-1)(1-0.5z^-1)(1-0.2z^-1))
    Y(z)((1-z^-1)(1-0.5z^-1)(1-0.2z^-1)) = X(z)(1-2z^-1+2z^-2-z^-3)
    Y(z)(1-1.7(z^-1)+0.8(z^-2)-0.1(z^-3)) = X(z)(1-2z^-1+2z^-2-z^-3)
    Y(z)-1.7Y(z)(z^-1)+0.8Y(z)(z^-2)-0.1Y(z)(z^-3) = X(z)-2X(z)(z^-1)+2X(z)(z^-2)-X(z)(z^-3)
    y[n]-1.7y[n-1]+0.8y[n-2]-0.1y[n-3] = x[n]-2x[n-1]+2x[n-2]-x[n-3]
    '''
    h = respuesta_al_impulso(100,
                             np.array([1, -2, 2, -1]),
                             np.array([1.7, -0.8, 0.1]))

    '''
  NOTA: segun el analicis de polos y ceros, podemos determinar que el sistema es estable,
  como podemos apreciar en la grafica de la respusta al impulso, que es finita.
  '''
    zplane(np.array([1, -2, 2, -1]), np.array([1, -1.7, 0.8, -0.1]))

    # GRAFICAS
    fig, ax = plt.subplots()
    ax.stem(h)
    ax.set_title('respuesta al impulso')
    ax.set_xlabel('n')
    ax.set_ylabel('h[n]')

    plt.show()


def ejer_4():
    def fun_en_s(s): return (12500*s)/((44*s**2)+(60625*s)+6250000)

    N = 5000
    w = np.arange(0, N)
    Hs = fun_en_s(1j*w)

    Hs_max = max(abs(Hs))
    id = np.nonzero(abs(Hs) == Hs_max)[0][0]

    for i in range(id, Hs.shape[0]):
        if abs(Hs[i]) < (Hs_max-3):
            break

    f = 4*i
    # f = 4*(i/(2*np.pi))
    T = 1/f
    print(f'periodo de muestre: T={T}')

    # aproximaciones
    def euler(z): return (1-z**(-1))/T
    def bilineal(z): return (2/T)*((1-z**(-1))/(1+z**(-1)))

    z = np.exp(1j*np.arange(0, np.pi, T))

    _, ax = plt.subplots(3, constrained_layout=True)
    ax[0].plot(abs(Hs))
    ax[0].set_title('aproximacion real')
    ax[0].set_xlabel('frecuencias')
    ax[0].set_ylabel('dB')
    ax[1].plot(abs(fun_en_s(euler(z)))[0:N])
    ax[1].set_title('transformacion de euler')
    ax[1].set_xlabel('frecuencias')
    ax[1].set_ylabel('dB')
    ax[2].plot(abs(fun_en_s(bilineal(z)))[0:N])
    ax[2].set_title('transformacion bilineal')
    ax[2].set_xlabel('frecuencias')
    ax[2].set_ylabel('dB')
    plt.show()


if __name__ == '__main__':
    ejer_2(fun_item_a)
    # ejer_3()
    # ejer_4()
