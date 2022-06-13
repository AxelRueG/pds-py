import numpy as np
import matplotlib.pyplot as plt

## -----------------------------------------------------------------------------
# retorna la evalucion del polinomio de legendre para un t discreto
# i: subindice del polinomio de legendre
# t: vector de tiempo discreto
def legendre(i,t):
  if (i == 0):
    return np.sqrt(0.5)*np.ones(t.size)
  elif (i == 1):
    return np.sqrt(1.5)*t
  elif (i == 2):
    return np.sqrt(2.5)*((1.5*(t**2))-0.5)
  elif (i == 3):
    return np.sqrt(3.5)*((2.5*(t**3))-(1.5*t))
  elif (i == 4):
    return np.sqrt(4.5)*((1.375*t**4)-(3.75*t**2)+(0.375))
  else:
    return np.sqrt(5.5)*((4.375*t**5)-(5*t**3)+(1.125*t))

## -----------------------------------------------------------------------------
# calcula y grafica el error cuadratico, resultado de variar los alfas de la 
# funcion aproximante
# n: tamanio de la matriz
# y: vector de valores de la funcion a aproximar
# l: matriz con las evaluaciones del polinomio de legendre

def matriz_de_errores(n,y,l):
  # sabemos que en el caso de la funcion f(t) = 1 si t>=0 o -1 si t<0
  # la aproximacion queda de la siguiente forma:
  # y ~ a1*l1+a3*l3 = (45/16)t-(35/16)t**3
  aproximacion = lambda a1,a3: a1*l[1]+a3*l[3]

  ap1 = np.sqrt(1.5)
  ap3 = -np.sqrt(7/32)
  alpha1 = np.linspace(ap1-0.3,ap1+0.3,n)
  alpha3 = np.linspace(ap3-0.3,ap3+0.3,n)

  mError = np.zeros([n,n])
  for i in range(0,n):
    for j in range(0,n):
      # calculamos el error cuadratico
      mError[i][j] = np.linalg.norm(y-aproximacion(alpha1[i],alpha3[j]))**2

  # ploteo
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  A1,A3 = np.meshgrid(alpha1,alpha3)
  ax.plot_surface(A1, A3, mError)


## -----------------------------------------------------------------------------
def ejer_3():
  # funcion del ejemplo  
  t = np.arange(-1,1,0.01)
  y = np.ones(t.size)
  y[np.nonzero(t<0)] = -1

  # calculamos los alphas
  a = np.zeros(6)
  l = np.zeros([6,t.size])
  for i in range(0,6):
    l[i,:] = legendre(i,t)
    # a = <v1,v2>/<v2,v2>
    a[i] = np.dot(y,l[i,:])/np.dot(l[i,:],l[i,:])
  

  aproximacion1 = a[0]*l[0]+a[1]*l[1]+a[2]*l[2]+a[3]*l[3]
  aproximacion2 = a[0]*l[0]+a[1]*l[1]+a[2]*l[2]+a[3]*l[3]+a[4]*l[4]+a[5]*l[5]

  print(f'error cuadratico con una aproximacion de 4: {np.linalg.norm(y-aproximacion1)**2}')
  print(f'error cuadratico con una aproximacion de 6: {np.linalg.norm(y-aproximacion2)**2}')

  img, ax = plt.subplots()
  ax.set_title('comparacion de apoximaciones')
  ## iniciso a
  ax.plot(t,y,label='y(t)')
  ax.plot(t,aproximacion1, label='aproximacion de 4 polinomios')
  ## iniciso c
  ax.plot(t,aproximacion2,'r', label='aproximacion de 6 polinomios')
  ax.legend()

  # iniciso b
  matriz_de_errores(15,y,l)

  plt.show()