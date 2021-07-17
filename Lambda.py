#Using lambda for creating functions
from functools import reduce
import math

circle_perimeter = lambda radius:2*3.14*radius

#Using filter() function
even_odd=[3,4,5,6,10,78,45,24]
evens=list(filter(lambda n :n%2==0,even_odd))
print(evens)

#Using map() function
odd=list(map(lambda x :x+2,even_odd))
odd1=list(filter(lambda x:x>10,evens))
print(odd)
print(odd1)
#print()
#Using reduce() function
sum =reduce(lambda a,b:a+b, evens)
print(sum)

print(math.radians(60))
print(ord('A'))









even_odd=[3,4,5,6,10,78,45,24]
evens=list(filter(lambda x: x%2==0, even_odd))
print(evens)

new=list(map(lambda x:x*2, evens))
print(new)
sum=reduce(lambda a,b:a+b, even_odd)
print(sum)


listA=[12,3,14,5,6]

listB=list(dict.fromkeys(listA))
print(sorted(listB))

str1="shalini"
str2=reversed(str1)
print(str2)



def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
print(result)


pairs=[(1,'one'),(2,'two'),(3,'three')]
print(sorted(pairs, key=lambda x:x[1]))

print(math.radians(60))
