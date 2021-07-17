import numpy as np

arr1=np.array(
    [
        [1,2,3,4,6,5,2,4],
        [8,9,10,11,12,13,23,24]
    ]
)
arr2=arr1.reshape(4,4)
print(arr2)

m=np.matrix(arr2)
print(m)
print(np.diagonal(m))
print(m.min())
print(m.max())

arr4=(
    [3,4],
    [5,6]
)
arr5=(
    [3,4],
    [5,6]
)
print(np.matrix(arr4)*np.matrix(arr5))

test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]
list1=list(map(''.join,test_list))
print(str(list1))

Input = ['first', 'second', 'third']
tuple=tuple(map(lambda x:[x],Input))
print(tuple)

str1="my name is John"
str2=" my son's name is Ishan"


