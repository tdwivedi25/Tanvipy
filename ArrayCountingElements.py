from array import*
from collections import Counter, OrderedDict

arr1=array('d',[5.3,6.8,7.2,1.5,6.8,7.2,6.8,1.5,5.3])



list1=list(arr1)
print(list1)
list1_counter=Counter(list1)#in collections module it counts the elements in a list.
print(list1_counter)
for k,v in list1_counter.items():
    print(k, 'count is', v)
print()
print()
print()
print()
print()


list1_ord=OrderedDict(list1_counter)
for k,v in list1_ord.items():
    print(k, 'count is', v)

#for x in list1:
#    y = list1.count(x)
#    print (set(x,y))

set1=list(arr1)
print(set1)
set1_counter=Counter(set1)#in collections module it counts the elements in a list.
print(set1_counter)
for k,v in list1_counter.items():
    print(k, 'count is', v)
print()
print()
print()
print()
print()


set1_ord=OrderedDict(list1_counter)
for k,v in set1_ord.items():
    print(k, 'count is', v)

