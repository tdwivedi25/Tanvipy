list1=[]
for i in range(1, 10):
    print("the binary conversion of {0} is".format(i),bin(i))
    list1.append(bin(i))
print()
print(list1)

for i in list1:
    print(i.lstrip('0b'),end=" ")

try:
  if x==1:
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
    print('it\'s over')

y=-1
if y < 0:
  raise Exception("Sorry, no numbers below zero")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")






