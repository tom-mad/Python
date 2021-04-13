#1
import sys
if len(sys.argv)==1:
  print('Brak argumentów na wejściu\nProszę przy uruchomieniu podać argumenty')
  sys.exit()
text = ''.join(sys.argv[1:])
print(text)

#2
small, big, num, d_ft=[],[],[],[]

for x in text:
  if x.isalpha():
    if x.isupper():
      big.append(x)
    else:
      small.append(x)
  else:
    if x.isnumeric():
      num.append(x)
    else:
      d_ft.append(x)
print(small)
print(big)
print(num)
print(d_ft)

#3
sm_l=[]
j=0
for i in small:
  if i not in sm_l:
    sm_l.append(i)
lista_skladana=[(i,small.count(i)) for i in sm_l] 
print(lista_skladana)
#4
lista_skladana.sort(reverse=True,key=lambda x:x[1])
print(lista_skladana)
#5   
samogloski = ['a','e', 'i', 'o', 'u', 'y','A','E','I','O','U','Y']
a,b=0,0
nume=[]
for i in text:
  if i.isalpha():
    if samogloski.count(i):
      a+=1
    else:
          b+=1
  else:
    if i.isnumeric():
      nume.append(i)
print(nume)
lista_5=[(int(x),a*int(x)+b) for x in nume] 
print(lista_5)
#6



