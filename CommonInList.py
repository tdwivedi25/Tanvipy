nums=[1,2,3,4,5,6,7,8,9,10]
print(nums)
even_nums=[1,4,6,90,7]
print(even_nums)
common=[]
for y in even_nums:
   print(end= '')
   if y in nums:
    #print(y,'is in both the lists')
    common.append(y)
print(len(common),'elements are common in both the lists')