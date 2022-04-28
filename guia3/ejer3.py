import numpy as np
import matplotlib.pyplot as plt
from Signals import senoidal

def ejer_3():
  legendre0 = lambda t: np.sqrt(0.5)*np.ones(t.size)
  legendre1 = lambda t: np.sqrt(1.5)*t
  legendre2 = lambda t: np.sqrt(2.5)*((1.5*t**2)-0.5)
  legendre3 = lambda t: np.sqrt(3.5)*((2.5*t**3)-(1.5*t))
  # legendre4 = lambda t: np.sqrt(4.5)*((1.375*t**4)-(3.75*t**2)+(0.375))
  # legendre5 = lambda t: np.sqrt(5.5)*((4.375*t**5)-(5*t**3)+(1.125*t))
  
  t,y = senoidal(0,1,64)
  a0 = np.dot(y,legendre0(t))
  a1 = np.dot(y,legendre1(t))
  a2 = np.dot(y,legendre2(t))
  a3 = np.dot(y,legendre3(t))
  print(a0)
  print(a1)
  print(a2)
  print(a3)

  pol = lambda t: a0*legendre0(t)+a1*legendre1(t)+a2*legendre2(t)+a3*legendre3(t)

  plt.plot(t,y)
  plt.plot(t,pol(t))
  plt.show()


