print("/////////////////////////\n","ZAD_1")
#1a

def returns_naturalNum():
  natural = 0
  while(True):
    natural+=1
    yield natural
#1b
def sum_allDivisors(num):
  sum = 0
  for i in range(1,num // 2+1):
    if num % i == 0:
      sum+=i
  return sum
def returns_perfectNum(seq):
  for i in seq:
    if i == sum_allDivisors(i):
      yield i
#1c
def returns_lessTmp(seq,tmp):
  for i in seq:
    if i<=tmp:
      yield i
    else:
      return
print("Liczby doskonałe:")
for i in returns_perfectNum(returns_lessTmp(returns_naturalNum(),1000)):
  print(i)
  
print("/////////////////////////\n","ZAD_2")

from math import log
def genUi():
  u,x,a= 0,1.,0.05
  while x <= 1.5:
    x += a
    u = u + a/x
    yield x,u,log(x)
  return
for i in genUi():
  print(i)

print("/////////////////////////\n","ZAD_3")
def numberEquation(n):
  tmp = 1
  while tmp < n:
    s,eq,fill=0,[],tmp
    while s != n:
      while s+fill > n:
        fill = fill-1
      s=s+fill
      eq.append(fill)
      fill=tmp
    tmp=tmp+1
    yield eq
  return

for i in numberEquation(10):
  print(i)

print("/////////////////////////\n","ZAD_4")
import random
def returnIF():
  randBot=random.random()
  if randBot<0.1:
    return
  while True:
    randTop=random.random()
    if randTop<0.1:
      return
    if abs(randTop-randBot)>=0.4:
      yield randTop
      randBot=randTop
for i in returnIF():
  print(i)
print("/////////////////////////\n","ZAD_5")

def range(start,stop=None,step=1.):
  if stop == None:
    stop=start
    start=0
  if step == 0:
    return
  if step>0:
    if start<stop:
      while start < stop:
        yield start
        start+=step
  else:
    if start>stop:
      while start > stop:
        yield start
        start+=step  
for i in range(8):
  print(i)
for i in range(-8):
  print(i)
for i in range(1,8):
  print(i)
for i in range(8,1):
  print(i)
for i in range(1,8,2):
  print(i)
for i in range(1,8,-2):
  print(i)
for i in range(8,1,-2):
  print(i)
for i in range(8,1,2):
  print(i)
for i in range(8,1,-2):
  print(i)
