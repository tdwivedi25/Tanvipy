from array import *
#Adding arrays using for loop
arr=array('i',[1,2,3,4,5,6])
tanu =array('i',[2,4,6,8,10,12])
newarr=array('i',[])
s=0

for e in arr:
        w=e+tanu[s]
        newarr.append(w)
        s += 1
print(newarr)
