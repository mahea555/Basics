print('******break*******')
stock = 5
x = int(input('how much quantity u want??'))
i=1
while i <= x:
    if i > stock:
        print('out of stock')
        break
    print('stock is available')
    i = i+1
print('******continue*******')

for i in range(1,101):
    if i % 3 == 0 or i % 5 ==0 :
        continue
    print(i)


print('******pass*******')

for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
