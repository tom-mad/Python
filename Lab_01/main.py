
#1.1
print('Zad.1.1')
list = [13,223,54,2,3,2,1,3,8,2,1]
print(list)
for x in range(list.count(2)):
    list.remove(2)
print(list)
#1.2
print('Zad.1.2')
k=0
list = [13,223,54,2,3,2,1,3,8,2,1]
print(list)
for x in range(len(list)):
    if list[x-k]==2:
        list.pop(x-k)
        k+=1
print(list) 
#2.
print('Zad.2')
list = [13,223,54,2,3,2,1,3,8,2,1,]
print(list)
while(list.count(2)):
    list.remove(2)
print(list)
#3.
print('Zad.3')
list = [13,223,54,2,3,2,1,3,8,2,1,]

for x in range(1,len(list),2):
    print(list[x])   
#4.
print('Zad.4')
list = [13,223,54,2,3,2,1,3,8,2,1,]
for x in list[1::2]:
    print(x)
#5.
print('Zad.5')
list = [13,223,54,2,3,2,1,3,8,2,]
for x in range(len(list)-1,0,-2):
    print(list[x])
#6.
print('Zad.6')
list = [13,223,54,2,3,2,1,3,8,2,]
for x in list[-1::-2]:
    print(x)
#7.
print('Zad.7')
list = [13,223,54,2,3,2,1,3,8,2,1,]
print(list)
for i in range(len(list)):
    list[i]=(i,list[i])
print(list)
#8
print('Zad.8')
list.sort(key=lambda x: x[1])
print(list)
#9
print('Zad.9')
list = [13,223,54,2,3,2,1,3,8,2,1,]
print(list)
ind=0
for i in range(len(list)):
    if(list[i]%2==0):
        list[i]=(ind,list[i])
        ind+=1
print(list)
print('Zad.10')
#10
list = [13,223,54,2,3,2,1,3,8,2,1,]
print(list)
for i in range(len(list)):
    if(list[i]>i):
        list[i]=(i,list[i])
    else:
        list[i]=(list[i],i)
print(list)