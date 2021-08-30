print("###############ZAD_1#################")
import abc
class Calka(abc.ABC):
  def __init__(self,xp,xk,n,f):
    self.xp,self.xk,self.n,self.f=xp,xk,n,f
  @abc.abstractmethod
  def solve(self):
    pass

class Trapez(Calka):
  def solve(self):
    s,h=0,(self.xk-self.xp)/self.n
    for i in range(self.n):
      s+=self.f(self.xp+i*h)+self.f(self.xp+i*h+h)
    return 0.5*h*s

class Simpson(Calka):
  def solve(self):
    s,h=self.f(self.xp),(self.xk-self.xp)/(2*self.n)
    for i in range(1,2*self.n,2):
      s+=4*self.f(self.xp+i*h)
    for i in range(2,2*self.n,2):
      s+=2*self.f(self.xp+i*h)
    s+=self.f(self.xk)
    return (h/3)*s

tr = Trapez(0,10,100,lambda x: x**2)
print(tr.solve())
si = Simpson(0,10,100,lambda x: x**2)
print(si.solve())
print("###############ZAD_2#################")
import random 
class Stack:
  def __init__(self,initStack=None):
    self.vector=[]
    if initStack:
      self.vector.extend(initStack.vector)
  def push(self,value):
    self.vector.append(value)
  def pop(self):
    self.vector.pop()
  def pushStack(self,bufferStack):
    self.vector.extend(bufferStack.vector)
  def __len__(self):
    return len(self.vector)
  def __str__(self):
    return f'{self.vector}'
class SortedStack(Stack):
  def __init__(self,rev=False):
    super().__init__()
    self.rev=rev
    self.vector.sort(reverse=self.rev)
  def push(self,value):
    if len(self.vector)==0:
      self.vector.append(value)
    if value>=self.vector[-1] and self.rev==False:
      self.vector.append(value)
    if value<=self.vector[-1] and self.rev==True:
      self.vector.append(value)
  def pushStack(self,bufferStack):
    if type(bufferStack) is SortedStack:
      for i in bufferStack.vector:
        self.push(i)
print("Rosnąco:")
s=0
for _ in range(100):
  tmp=SortedStack()
  for _ in range(100):
    tmp.push(random.randint(0,100))
  #print(tmp)
  s+=len(tmp)
print("Średnia Długość: ",s/100)
print("Malejąco:")
s=0
for _ in range(100):
  tmp=SortedStack(True)
  for _ in range(100):
    tmp.push(random.randint(0,100))
  #print(tmp)
  s+=len(tmp)
print("Średnia Długość: ",s/100)
