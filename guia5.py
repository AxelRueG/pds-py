import numpy as np

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
  Y(z)-Y(z)(z^-1)-Y(z)(z^-2) = X(z)
  Y(z)(1-(z^-1)-(z^-2)) = X(z)
  H(z) = Y(z)/X(z) = 1/(1-(z^-1)-(z^-2))

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



if __name__=='__main__':
  pass