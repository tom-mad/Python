import random
#1
k=20
ran=[random.randrange(0,5*k) for i in range(k)]
print("Wylosowana lista:\n",ran)

ranOld=ran[:]
s={}

for i in range(100):
  random.shuffle(ran)
  s[i+1]=0
  for j in range(len(ran)):
    if ran[j]==ranOld[j]:
      s[i+1]+=1
  ranOld=ran[:]
print("Ilość elementów która pozstała na swoim miejscu w każdej iteracji\n",s)

#2 losowy string
buffer="qwertyuiopasdfghjklzxcvbnm"
ran_str=""
for i in range(k):
  ran_str+=random.choice(buffer)+"."
print("Wylosowany string:\n",ran_str)

#3
ran_list=[random.randrange(0,20) for i in range(100)]
print("Wylosowana lista 100 elementowa z przedziału[0,20):\n",ran_list)
#3.1
dict_1={}
for i,j in enumerate(ran_list):
  dict_1.setdefault(j,[]).append(i)
print("Stworzony słownik pierwszą metodą:",dict_1)

#3.2
dict_2={}
for i in ran_list:
  dict_2.setdefault(i,[]).append(ran_list.index(i))
print("Stworzony słownik drugą metodą:",dict_2)

#4
n=random.randint(3,6)
limit_d=pow(10,n-1)
limit_g=pow(10,n)-1
s=0
for i in range(1000):
  x=random.randint(limit_d,limit_g)
  #y=str(x)
  #print(y)
  #y.reversed()
  #print(y)

#5
dict_1={}
dict_2={}
dict_1_rev={}
dict_2_rev={}
for i in range(10):
  dict_1[i+1]=random.randint(1,99)
  dict_1_rev[dict_1[i+1]]=i+1
  dict_2[i+1]=random.randint(1,99)
  dict_2_rev[dict_2[i+1]]=i+1

print("\nSłownik_1",dict_1,"\nSłownik_1 odwrócony\n",dict_1_rev,"\nSłownik_2\n",dict_2,"\nSłownik_2 odwrócony\n",dict_2_rev)
dict_end={}
for i in dict_1_rev:
    if i in dict_2_rev:
        dict_end[i]=(dict_1_rev[i],dict_2_rev[i])
print("Nowy Słownik:\n",dict_end)

