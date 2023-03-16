import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# func: funcion de senial (senoidal, cuadrada, ...)
# afin: si los alphas de la combinacion suman 1
# phi: si las seniales presentan desfase
def ejer_4(func, afin=False, phi=False):
    fm = 100  # frecuencia de muestreo
    phis = (2*np.pi*np.random.rand(10)) if phi else np.zeros(10)

    # matriz de seniales de freciencia [1:10]
    S = np.zeros([10, fm])
    for i in range(0, 10):
        t, S[i, :] = func(0, 1, fm, i+1, phis[i])

    # combinacion lineal
    alpha = np.random.rand(10)
    if afin:
        alpha = alpha/sum(alpha)

    Sn = np.zeros(fm)
    for i in range(0, 10):
        Sn += alpha[i]*S[i, :]

    # plot
    fig, ax = plt.subplots(2, 1)
    ax[0].stem(t, Sn)
    ax[0].set_title('senial combinada')
    ax[0].grid()
    ax[1].bar(np.arange(1, 11), np.dot(S, Sn))
    ax[1].set_title('grado de similitud')
    plt.show()
