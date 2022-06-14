import numpy as np

def rectangular(N):
  return np.ones(N)

def hanning(N):
  n = np.arange(N)
  w = 0.5-0.5*np.cos(2*np.pi*n/N)
  return w

def hamming(N):
  n = np.arange(N)
  w = (27/50)-((23/50)*np.cos(2*np.pi*n/N))
  return w

def bartlett(N):
  n = np.arange(N)
  w = 2*n/N
  case2 = np.nonzero(n>N/2)
  w[case2] = 2-2*n[case2]/N
  return w

def blackman(N):
  n = np.arange(N)
  w = (21/50) - ((1/2)*np.cos(2*np.pi*n/N)) + ((2/25)*np.cos(4*np.pi*n/N))
  return w