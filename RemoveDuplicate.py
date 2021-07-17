#Removing duplicates from a list using set
nums=[1,2,4,6,1,4,3,6,8,1]
print(nums,"- original list")
x = set(nums)
print(list(x),"-list after removing the duplicate item")

print()
#Removing duplicates from a list without using set
nums1=[]
print(nums,'-original list')
for x in nums:
    if x not in nums1:
        nums1.append(x)

print(nums1,'-list after removing the duplicate item')
