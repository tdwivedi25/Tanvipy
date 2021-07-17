from array import *
array1 = array('i',  [10,20,
                      30,40,50,60,70])

array1.insert(6,80)
for x in array1:
    print (x)
array1.remove(40)
print(array1.index(20))
for x in array1:
    print (x)




