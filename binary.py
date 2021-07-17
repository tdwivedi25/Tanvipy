import collections
import numpy as np

# creating an array
gfg = np.array([1, 2, 3, 4, 5, 6])
print(gfg.reshape(2, 3))
str1="shalini"
res=collections.Counter(str1)
print(res)



num=8
one_sum=0
bin_rep=bin(num)[2:]
for i in bin_rep:
    one_sum+=int(i)
print(one_sum)

for i in range(1, 10):
    print(bin(i))

list1=[]
for i in range(1, 10):
   list1.append(bin(i)[2:])
print(list1)
for j in list1:
    print(collections.Counter(j))





