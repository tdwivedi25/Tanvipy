#rom collections import *
nums=[0,1,2,3,0,4,5,6,7,0,8,9,10,0,11,12,13,0,'😊😊😊']
for x in nums:
    if x==0:
        nums.remove(0)
        nums.append(0)
print(nums)