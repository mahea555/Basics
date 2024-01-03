from functools import reduce

num=[1,3,5,7,4,8,9,2]

f=list(filter(lambda n : n%2==0, num)) #using lambda as function in function.

print(f)

x=list(map(lambda n : n*2,f)) #use of map

print(x)

y=reduce(lambda a,b : a + b, num) #use of reduce for that we have to import funtion first


print(y)