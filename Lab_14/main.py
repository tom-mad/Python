print("###############ZAD_1#################")
class Point2D:
  def __init__(self):
    self.x=0
    self.y=0
  @property
  def x(self):
    return self._x
  @x.setter
  def x(self,val):
    self._x=val
  @x.getter
  def x(self,val):
    return self._x
  @property
  def y(self):
    return self._y
  @y.setter
  def y(self,val):
    self._y=val
  @y.getter
  def y(self,val):
    self._y=val

obj = Point2D()
Point2D.x=3
Point2D.y=1
print(Point2D.x,Point2D.y)


print("###############ZAD_2#################")
def checkRange(x1,x2,y1,y2):
  def fz(pf):
    def fw(point1,point2):
      if x1<point1.x<x2 and x1<point2.x<x2 and y1<point1.y<y2 and y1<point2.y<y2 :
        return pf(point1,point2)
      else:
        raise Exception("Punkt poza zakresem!")
    return fw
  return fz
@checkRange(0,100,0,100)
def add(point1,point2):
  resultPoint = Point2D()
  resultPoint.x=point1.x+point2.x
  resultPoint.y=point1.y+point2.y
  return resultPoint

@checkRange(0,100,0,100)
def sub(point1,point2):
  resultPoint = Point2D()
  resultPoint.x=point1.x-point2.x
  resultPoint.y=point1.y-point2.y
  return resultPoint

p1 = Point2D()
p2 = Point2D()
p1.x = 10
p1.y = 15
p2.x = 5
p2.y = 7
print("Punkt 1:",p1.x,p1.y)
print("Punkt 2:",p2.x,p2.y)
pResult = add(p1,p2)
print("Po dodaniu p1+p2:",pResult.x,pResult.y)
pResult = sub(p1,p2)
print("Po odjęciu p1-p2:",pResult.x,pResult.y)
p1.x = 102
#print("Punkt p1.x poza zakresem:")
#add(p1,p2)


print("###############ZAD_3#################")
import math
class Figures:
  def __init__(self):
    pass
  @staticmethod
  def lenghtLine(a,b):
    return math.sqrt((b.x-a.x)**2+(b.y-a.y)**2)
  @staticmethod
  def triangleLenght(a,b,c):
    lenght=0 
    lenght += Figures.lenghtLine(a,b)
    lenght += Figures.lenghtLine(c,a)
    lenght += Figures.lenghtLine(c,b)
    return lenght
  @staticmethod
  def triangleArea(a,b,c):
    p = Figures.triangleLenght(a,b,c)/2
    return math.sqrt(p*(p-Figures.lenghtLine(a,b))*(p-Figures.lenghtLine(c,b))*(p-
    Figures.lenghtLine(c,a)))
  @staticmethod
  def quadrangleLenght(a,b,c,d):
    lenght=0 
    lenght += Figures.lenghtLine(a,b)
    lenght += Figures.lenghtLine(b,c)
    lenght += Figures.lenghtLine(c,d)
    lenght += Figures.lenghtLine(d,a)
    return lenght
  @staticmethod
  def quadrangleArea(a,b,c,d):
    p = Figures.quadrangleLenght(a,b,c,d)/2
    return math.sqrt((p-Figures.lenghtLine(a,b))*(p-Figures.lenghtLine(b,c))*(p-
    Figures.lenghtLine(c,d))*(p-
    Figures.lenghtLine(d,a)))
    pass 
p1 = Point2D()
p2 = Point2D()
p3 = Point2D()
p1.x = 0
p1.y = 0
p2.x = 0
p2.y = 3
p3.x = 4
p3.y = 0
print("Pole Trójkąta o dłguościach boków 3,4,5 = ",Figures.triangleArea(p1,p2,p3))
p4 = Point2D()
p1.x = 0
p1.y = 0
p2.x = 0
p2.y = 4
p3.x = 4
p3.y = 4
p4.x = 4
p4.y = 0
print("Pole czworokąta o długościach boku 4 = ",Figures.quadrangleArea(p1,p2,p3,p4))
