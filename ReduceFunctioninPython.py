from functools import reduce
#Using lambda for creating functions
circle_perimeter = lambda radius:2*3.14*radius

#Using filter() function
even=[3,4,5,6,10,78,45,24]
evens=list(filter(lambda n :n%2==0,even))
print(evens)

#Using map() function
odd=list(map(lambda x :x>70,evens))
print(odd)

#Using reduce() function
#sum = list(reduce(lambda y:y+2,odd))