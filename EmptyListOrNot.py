x = int(input('Enter the length of the list : '))


y=[]
for i in range(0,x):
    item = input('Enter an element :')
    y.append(item)
print(y)

if len(y)==0:
    print('This is an empty list.')
else:
    print('This is not an empty list,the length of the list is {0} items'.format(len(y)))