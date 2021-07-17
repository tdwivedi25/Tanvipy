
def eurotousd(euro,rate=0.8):
    return euro*rate
print(eurotousd(10))

x = 10.0

if type(x) == float:
    print(int(x))
else:
    print(x)



items = ['adapter', 'cable', 'keyboard']

choice = input("Item")
if choice in items:
    print("Item is available!")

w=float(input('Weight: '))
price=w*2.5
print(f'Price is {price}')



for letter in 'abc':
    print(letter.upper())

for item in [[1, 2, 3], [4, 5, 6]]:
    print(item[0])

x = [len(item) for item in ['abc', 'def', 'ghi']]
print(x)

y = [i * 2 if i > 0 else 0 for i in [1, -2, 10]]



def foo(a = 1, b = 'John'):
    return a + b
foo()

mylist = [['abc'], ['def', 'ghi']]
mylist[-1][-1][-1]

def foo(x):
    return x ** 2
print(foo("Hello"))