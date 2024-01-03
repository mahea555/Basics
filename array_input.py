from array import *
a = array('i',[]) #empty array

n= int(input('Enter the lenth of array'))

for i in range(n):
    x=int(input('Enter the value'))
    a.append(x)

print(a)

print('************searching index of value using loop*************************')

val=int(input('enter the value u want to search'))
k=0
for i in a:
    if val==i:
        print(k)
        break
    k=k+1
print('************searching index of value using function*************************')

print(a.index(val))