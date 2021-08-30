def printPascal(n):
  '''
  Funkcja wyświetlająca trójkąt Pascala o rozmiarze n(argument funkcji)
  '''
  space = n
  mem = [0]
  current = [1]
  for _ in range(n):
    for _ in range(space):
      print(' ',end='')
    space-=1
    print(current)
    current=[l+r for l,r in zip(current+mem,mem+current)]
  return 

def Newton(n,k):
  if k == 0:
    return 1
  elif n == k or n==0:
    return 0
  else:
    return  (k+1)*Newton(n-1,k)+(n-k)*Newton(n-1,k-1)
def printEuler(n):
  '''
  Funkcja wyświetlająca trójkąt Eulera o rozmiarze n(argument funkcji)
  '''
  print("n/k",end="")
  for i in range(n+1):
    print("  ",i,end="")
  print("")
  for i in range(n+1):
    print(i,"    ",end="")
    for j in range(n+1):
      print(Newton(i,j),"  ",end="")
    print("")

import string
def make_codeCezar(file,shift):
  '''
  Funkcja kodujaca szyfrem cezara, przesunięcie liter jest o zadana wartość shift
  '''
  cezarText=""
  with open(file,"r") as Text:
    normalText=Text.read()
    for character in normalText:
      tmp=ord(character)+shift
      cezarText+=chr(tmp)
  cezarFile=open("cezarText.txt","w")
  cezarFile.write(cezarText)
  cezarFile.close()

def read_codeCezar(file,shift):
  '''
  Funkcja odczytujaca szyfr Cezara znajac przesuniecie
  '''
  normalText=""
  with open(file,"r") as Text:
    cezarText=Text.read()
    for character in cezarText:
      tmp=ord(character)-shift
      normalText+=chr(tmp)
  normalFile=open("normalText.txt","w")
  normalFile.write(normalText)
  normalFile.close()





  