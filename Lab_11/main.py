print("###############ZAD_1#################")
import matplotlib.pyplot as plt
import random

class IFS:
  def __init__(self,f,prob):
    self._factors=f
    self._x,self._y=[0],[0]
    self._prob=prob
  def makeTrans(self,iter):
    for i in range(iter):
      l = random.choices(self._factors,self._prob)[0]
      self._x.append(l[0]*self._x[i]+l[1]*self._y[i]+l[2])
      self._y.append(l[3]*self._x[i]+l[4]*self._y[i]+l[5])
  def draw(self):
    plt.plot(self._x,self._y,'.')
    plt.show()

chart = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
chart.makeTrans(10000)
chart.draw()

print("###############ZAD_2#################")

from math import sqrt

class Wektor:
  def __init__(self,x=0,y=0,z=0):
    self._x=x
    self._y=y
    self._z=z
  def __add__(self,vect):
    return Wektor(self._x+vect._x,self._y+vect._y,self._z+vect._z)
  def __sub__(self,vect):
    return Wektor(self._x-vect._x,self._y-vect._y,self._z-vect._z)
  def __mul__(self,val):
    self._x*=val
    self._y*=val
    self._z*=val
  def __str__(self):
    return f'x = {self._x}, y = {self._y}, z = {self._z}'
  def lenVect(self):
    return sqrt(self._x**2+self._y**2+self._z**2)
  def multiScalar(self,vect):
    return self._x*vect._x+self._y*vect._y+self._z*vect._z
  def multiVect(self,vect):
    return Wektor(self._y*vect._z-self._z*vect._y,self._z*vect._x-self._x*vect._z,self._x*vect._y-self._y*vect._x)
  def mixMulti(self,vect_1,vect_2):
    return self.multiScalar(vect_2.multiVect(vect_1))

v0 = Wektor(1,2,3)
v1 = Wektor(4,5,6)
v2 = v0 + v1
print(v0)
print(v1)
print(v2)
v0*5
print(v0)
print(v0.lenVect())
print(v0.multiScalar(v1))
print(v0.multiVect(v1))
print(v1.mixMulti(v0,v2))

print("###############ZAD_3#################")

def magneticFlux(B,S):
  return B.multiScalar(S) 
def Lorentz_Force(q,E,v,B):
  return q*(E+v.multiVect(B))
def workLorentz(q,E,v):
  return q * E.multiScalar(v)
