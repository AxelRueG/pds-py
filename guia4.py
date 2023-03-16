from guia4.ejer1 import ejer1
from guia4.ejer2 import ejer2
from guia4.ejer3 import ejer3
from guia4.ejer4 import ejer4
from guia4.ejer5 import ejer5
from guia4.ejer6 import ejer6
from utils.ventanas import bartlett, hamming, hanning, rectangular, blackman

import numpy as np

if __name__ == "__main__":
    # ejer1(tf=2,f1=10,f2=10.5,fm=1000)
    # ejer2(inciso=0)
    # ejer3(fs=10,fm=100,despazamiento=10)
    # ejer4(bartlett, 'bartlett')
    ejer5(fm=50, fs=105)
    # ejer6()
