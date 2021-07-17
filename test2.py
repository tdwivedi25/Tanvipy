from functools import reduce

lambdasum=lambda a,b: a+b

res=lambdasum(3,4)
print(res)

largest=lambda x, y: x if x>y else y

print(largest(5.2, 6.9))

list1=[3,4,5,6,7,8]
print(list(filter(lambda x: x%2==0, list1)))

list1=[3,4,5,6,7,8]
print(list(filter(lambda x: x%2 !=0, list1)))

print(reduce(lambda x, y:x+y, list1))
print(list(map(lambda x: x*2, list1)))