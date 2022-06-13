import numpy as np
from scipy.io import wavfile

from guia3.ejer5 import senial_desfasada
from os.path import abspath

def ejer_6():
  samplerate, data = wavfile.read(abspath('./datasets/escala.wav'))
  tono_longitud = round(data.size/8)

  position = -1
  parecido = -1000
  fa_fs = 349.23
  for i in range(0,8):
    p = senial_desfasada(fa_fs,data[tono_longitud*i:tono_longitud*(i+1)])
    # print(p)
    if parecido<p: 
      parecido = p
      position = i
  
  print(f'el tono FA es el numero {position} en el audio')
