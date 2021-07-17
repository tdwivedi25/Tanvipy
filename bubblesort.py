'''bubblesort'''
def bubble(alist):
 for passnum in range(len(alist)-1,0,-1):
    for i in range(passnum):
        if alist[i]>alist[i+1]:
            temp=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=temp
alist=[54,36,26,18,21,43,67,23]
print(len(alist))
bubble(alist)
print('output')
print(alist)



