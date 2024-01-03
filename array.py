from array import *
a= array('i',[24,53,64,75,86,47])
print(a)


for i in a:
    print(i)

print('*************Alt way************************')

for i in range(len(a)):
    print(a[i])

print('**************Using While loop***********************')

x=0
while x < len(a):
    print(a[x])
    x=x+1


print('************copy array*************************')


new_a=array(a.typecode,(x*x for x in a))

print(new_a)


print('************copy array*************************')



