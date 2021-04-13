import random
import sys

#1
print("zad1")

def rownanie(text):
  wyniki=[(x:=random.random(),eval(text)) for _ in range(10)]
  return wyniki


if len(sys.argv)==1:
  print("Brak argumentow")
  sys.exit()
text = ''.join(i for i in sys.argv[1] if i.isalpha() and  i!="x")
podmiana = str.maketrans(text,''.join(str(random.randrange(10)) for i in range(len(text))))
text = ''.join(sys.argv[1])
text=text.translate(podmiana)
print(text)
print(rownanie(text))

#2
print("zad2")
def create_list(*lists_in):
  wynik=[]
  for i in lists_in[0]:
    for j in  lists_in[1:]:
      if i not in j:
        break
    else:
      wynik.append(i)
  return wynik

print(create_list([1,2,3], (1,3,5), [3,2,1]))
#3
print("zad3")

def seq(seq_1,seq_2,check=True):
  if(check):
    wyniki=[(seq_1[i],seq_2[i]) for i in range(len(seq_1)) if i<len(seq_2)]
    return wyniki
  else:
    wyniki=[(seq_1[i] if len(seq_1)>i else None,seq_2[i]if len(seq_2)>i else None) for i in range(100) if len(seq_1)>i or len(seq_2)>i]
    return wyniki

print(seq([1,2,5,6],[1,2,3],False))
#4
print("zad4")

def money_back(money,type_money = (10,5,2)):
  cash=[]  
  for i in type_money:
    if money>0:
      cash.append((i,money // i*i))
      money=money - money // i*i
  if money!=0:
    print("Reszta nie wydana: ",money)
  else:
    print("Całkowicie rozmieniono")
  return cash;

print(money_back(24))

#5
print("zad5")

def look_for(integer,lower_limit,upper_limit,method="r"):
  steps_counter = 0;
  if method=="r":
    print("Wyszukiwna metodą losującą:")
    while True:
      steps_counter+=1
      tmp=random.randint(lower_limit,upper_limit+1)
      if tmp == integer:
        break
      lower_limit+=1 if tmp<integer else 0
      upper_limit-=1 if tmp>integer else 0
  else:
    print("Wyszukiwana metodą podziału")
    while True:
      steps_counter+=1
      tmp=lower_limit+((upper_limit-lower_limit)//2)
      if tmp == integer:
        break
      lower_limit=lower_limit if tmp>integer else tmp
      upper_limit=upper_limit if tmp<integer else tmp
  print("Wykonano ",steps_counter,"kroków")

look_for(5,3,54,'a')    
look_for(5,3,54)    
        
