print('***************writing simple function*********')

def add_sub(x,y):
    a = x + y
    b = x - y
    print(a,b)

add_sub(5,3)
print('***************writing simple function*********')

def add_sub(x,y):
    a = x + y
    b = x - y
    return a,b

add,sub= add_sub(5,4)
print(add,sub)

print('***************writing variable lenth function*********')

def cal(a, *b): #here *b means it can take many arguments and that arguments form a tuple.
    print(a)
    print(b)

cal(1,2,3,4,5,6)

print('***************writing variable lenth function*********')

def cal(a, *b): #here *b means it can take many arguments and that arguments form a tuple.
    c=a
    for i in b:
        c=c+i
    print(c)

cal(1,2,3,4,5,6)


print('***************writing variable lenth function with key*********')

def person(name, **data): #here ** bcoz of to accept parameter with key
    print(name)
    print(data)

person('Mahen', age=29, city='pune')

print('***************writing variable lenth function with key and values*********')

def person(name, **data): #here ** bcoz of to accept parameter with key
    print(name)
    for i,j in data.items():
        print(i,j)

person('Mahen', age=29, city='pune')

print('***************writing global variable *********')

a=10
def ex():
    a=9
    x=globals()['a']
    print('inside',a)
    print(x)
    globals()['a']=15

ex()
print('outside',a)

print('***************writing fuc getting list as argument *********')

def count(lst):
    e=0
    o=0
    for i in lst:
        if i%2==o:
            e+=1
        else:
            o+=1
    return e,o

lst=[12,58,65,87,97]

e,o=count(lst)
print('even no.:{} and odd no is:{}'.format(e,o))