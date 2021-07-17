from numpy import *

#Array method
arr = array([23,12,34,56,78])
print(arr)
for i in arr:
    print(i)

#Linspace method
arr1 = linspace(0,10)
print(arr1)

#Logspace method
arr2 = logspace(1,8,5)
print(arr2)
print('%.2f' %arr[1])

#Arrange method
arr3 = arange(1,20,3)
print(arr3)

#Zeros and Ones method
arr4 = zeros(6)
print(arr4)

arr4 = ones(6)
print(arr4)

#Adding arrays(vectorized operation)
arr5 = array([1,2,4,5,6])
arr6=arr5+10
print(arr6)

arr7=arr+arr5
print(arr7)

arr8=arr5
print(arr8)
print(sum(arr5))

print(id(arr8))
print(id(arr5))
#Copying arrays

arr8=arr5.view()
print(id(arr8))
print(id(arr5))

arr9=array([1,8,7,4,5])

arr9[1]=11
print(arr9)

arr10=arr9.copy()
print(arr10)

print(id(arr9))
print(id(arr10))


print(arr9.ndim)