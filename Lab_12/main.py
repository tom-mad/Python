print("###############ZAD_1#################")
#1.1
class iter_oneClass:
  def __init__(self,mx):
    self.max = mx
    self.min=-1
  def __iter__(self):
    return self
  def __next__(self):
    self.min+=1
    if self.min == 0:
      self.F2=0
      return 0;
    if self.min == 1:
      self.F1=1
      return 1  
    F = self.F1+self.F2 
    self.F2 = self.F1
    self.F1 = F
    if self.min < self.max:
      return F
    raise StopIteration

oneClass = iter_oneClass(9)
print("Pierwsza iteracja jedna klasa:")
for i in oneClass:
  print(i,end=' ')
print()
#w tym przypadku wartosci sa zapamietane dlatego nie ma wypisywania
print("Druga iteracja jedna klasa:")
for i in oneClass: 
  print(i,end=' ')
print()
#1.2
class iter_twoClass:
  def __init__(self,mx):
    self.max = mx
  def __iter__(self):
    return iterNext(self.max)
class iterNext:
  def __init__(self,mx):
    self.max = mx
    self.min=-1
  def __next__(self):
    self.min+=1
    if self.min == 0:
      self.F2=0
      return 0;
    if self.min == 1:
      self.F1=1
      return 1  
    F = self.F1+self.F2 
    self.F2 = self.F1
    self.F1 = F
    if self.min < self.max:
      return F
    raise StopIteration

twoClass = iter_twoClass(9)
print("Pierwsza iteracja podwójną klasa:")
for i in twoClass:
  print(i,end=' ')
print()
#w tym przypadku nie ma tego problemu co powyzej
print("Druga iteracja podwójną klasa:")
for i in twoClass:
  print(i,end=' ')
print()
print("###############ZAD_2#################")
import random

class iter_pseudoRandom:
  def __init__(self,m,a,c,x0):
    self._m,self._a,self._c,self._x=m,a,c,x0
  def __iter__(self):
    return self
  def __next__(self):
    self._x=(self._a*self._x+self._c)%self._m
    return self._x/self._m

pseudoRandom = iter_pseudoRandom(2**31-1,7**5,0,1)
def point_inSquare(point,sideSq):
  if sideSq >= point[0] and sideSq >= point[1]:
    return 1
  return 0
sumOurRandom=[0 for _ in range(10)]
sumBuiltInRandom=[0 for _ in range(10)]

for i in range(10**5):
  OurRandom=(next(pseudoRandom),next(pseudoRandom))
  BuiltInRandom=(random.random(),random.random())
  for n in range(1,11):
    sumOurRandom[n-1]+=point_inSquare(OurRandom,n*0.1)
    sumBuiltInRandom[n-1]+=point_inSquare(BuiltInRandom,n*0.1)
print("Nasze Losowania:\n",sumOurRandom)
print("Losowanie z użyciem funkcji wbudowanej:\n",sumBuiltInRandom)
print("###############ZAD_3#################")

import scipy.misc
from math import sin
class approxOfZero:
  def __init__(self,funct,x,eps):
    self._funct,self._x,self._eps=funct,x,eps
  def __iter__(self):
    return self
  def __next__(self):
    xMem=self._x
    self._x=xMem-self._funct(xMem)/scipy.misc.derivative(self._funct,xMem)
    if abs(self._x-xMem)<self._eps:
      raise StopIteration
    return self._x
zeros = approxOfZero(lambda x:sin(x)-(0.5*x)**2,1.5,10**-5) 
print("Kolejne przybliżenia miejsc zerowych:")
for i in zeros:
  print(i)

