print("zad1")###########################################################

import time
import sys

powt=1000
N=10000

def forStatement():
  lists=[]
  for i in range(N):
    lists.append(i+i)
  return lists
def listComprehension():
  return [i+i for i in range(N)]
def mapFunction():
  return map(lambda i:i+i,range(N))
def generatorExpression():
  return (i+i for i in range(N))

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

def tester(testFunction):
  t = time.time_ns()
  for _ in range(powt):
    testFunction()
  return abs(t-time.time_ns())

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
'''
1)i
forStatement         => 3541383586
listComprehension    => 1741227126
mapFunction          => 1626714
generatorExpression  => 1632499
2)i+i
forStatement         => 2485338134
listComprehension    => 1607406844
mapFunction          => 859378
generatorExpression  => 894615
3)i+(i**2)
forStatement         => 7363089056
listComprehension    => 8326235299
mapFunction          => 1018856
generatorExpression  => 997135
4)sumowanie petla
forStatement         => 3270999866
listComprehension    => 1890471320
mapFunction          => 4298710914
generatorExpression  => 3602996435
5)suma z wykorzystaniem sum()
forStatement         => 1952849190
listComprehension    => 1019768250
mapFunction          => 1990577282
generatorExpression  => 1013680286
6)map i generator konwersja do listy za pomoca list()
forStatement         => 3175916429
listComprehension    => 1696923512
mapFunction          => 3528918355
generatorExpression  => 2081288157
'''
print("zad2")###################################
from math import sqrt
import random

r = 1
a = 2
P_square = a*a
n=1000 #ilosc krokow
l=len(list(filter(lambda x: x<=r ,[sqrt(random.uniform(-1,1)**2+random.uniform(-1,1)**2) for _ in range(n)])))
pi=l*P_square/n
print(pi)
print("zad3")######################################

matrix_1=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
  ]
matrix_2=[
  [7,8,6],
  [1,2,3],
  [4,5,9]
  ]
#3.1
print(list(map(max,matrix_1)))

#3.2
print(list(map(max,zip(*matrix_1))))

#3.3
print([list(map(sum, zip(*i))) for i in zip(matrix_1, matrix_2)])

print("zad4")######################################
import functools

l = [
  [6,3],
  [4,9],
  [5,3],
  [0,1]
  ]
result = functools.reduce(lambda a,b:[a[0]+[b[0]],a[1]+[b[1]]],l,[[],[]])
print(result)

print("zad5")######################################

def lineCoefficients(xPoints,yPoints):
  n=len(xPoints)
  x_=sum(xPoints)/n
  D=sum(list(map(lambda x:(x-x_)**2,xPoints)))
  a=sum(list(map(lambda x,y:y*(x-x_)/D,xPoints,yPoints)))
  b=sum(yPoints)/n-a*x_
  print(a," ",b)
  dY=sqrt(sum(list(map(lambda x,y:(y-(a*x+b))**2,xPoints,yPoints))))
  dA=dY/sqrt(D)
  dB=dY*sqrt((1/n)+(x_**2/D))
  return {
    "współczynnik a": a,
    "współczynnik b": b,
    "niepewność współczynnika a": dA,
    "niepewność współczynnika b": dB,
  }
print(lineCoefficients([1,2,3.4,4,5],[1,2,3,4,5]))