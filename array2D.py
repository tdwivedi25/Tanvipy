from numpy import *
arr1=array([
    [1,2,3],
    [4,5,6]
])

arr2=array([
    [4,6,7],
    [7,8,9]
])

arr4=arr1+arr2
print(arr4)



print(arr1)
print(arr1.size)
print(arr1.shape)
arr2=arr1.flatten()
print(arr2)
arr3=arr2.reshape(3,2)
print(arr3)

