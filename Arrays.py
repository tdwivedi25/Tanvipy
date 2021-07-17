from array import *



#defined array by importing array module
vals=array('i',[1,2,4,5,7])
print(vals)

#printing the address and size of array in tuple
print(vals.buffer_info())

#printing the type of array
print(vals.typecode)

# reversing the array
vals.reverse()
print(vals)

#copying the array to another array
vals1=array('I',[11,12,13,14,15,16])
newArr=array(vals1.typecode,(a for a in vals1))
print("New Array is: ",newArr)
#arrranging the array in ascending order
arr = array('i',[11,2,32,41,5,6])
#print(arr.sort())
#User input
x =array('i',[])#telling the type of array and creatingan array
y = int(input('Enter the size of the array : '))
for i in range (y):
    w = int(input('Enter an integer : '))
    x.append(w)
    print(x)
print(x)

#Searching an element in an array
arr2 =array('i',[23,34,56,78,90])
w =int(input('Enter the number you want to search: '))
print(arr2.index(w))
"""
k=0
for e in arr2:
    if e == w:
        print(k)
    k+=1
"""