#LIST
num= [12, 34, 35, 56, 67, 89, 90]
print(num)
#print index wise
print(num[0])
print(num[5])
print(num[0:3])
# we can print it in reverse order by using - sign.
print(num[-7:])
print(num[-1])
#****************************************************
#we can make list of all data types indiviadually or togather.
name=['mahe', 'hema', 'raj', 'rani']
print(name)
mix =['mahe', 'hema', 25, 1.7]
print(mix)
#we can also have list of list
combo = [name, num]
print(combo)
print(combo[0])
print(name[1])
print(name.count('mahe'))

#*************************************************
set={'mahe', 'hema', 12, 55}
print(set)
print(set)

#************************************Dictionary*****************

d={'mahe':'Iphone', 'hema':'Nokia', 'raj':'vivo', 'mob': 9527608475}
print(d)
print(d.values())
print(d.keys())
print(d['mob'])


#*********************************************Range****************
a=range(10)
print(a)
print(list(a))
b=range(2,50,2)
print(b)
print(list (b))