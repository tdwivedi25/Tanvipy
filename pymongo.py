from logging import exception

x=1
y=0
try:
    z=x/y
    print(z)
except ZeroDivisionError as err:
    print(err)
finally:
    print("welcome to this world")


while True:
  try:
     x = int(input("Please enter a number: "))
     break
  except ValueError:
     print("Oops!  That was no valid number.  Try again...")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair:pair[0])
print(pairs)

nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0, nums))
print(evens)
