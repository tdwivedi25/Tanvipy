from array import *
#Searching an element in an array
arr2 =('i',[23,34,56,78,90])
w =int(input('Enter the number you want to search: '))
k=0
for e in arr2:
    if e ==w:
        print(k)
        break
    k+=1