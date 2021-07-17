#Finding the greatest number form the list
nums=[5,1,4,2,6,7,9]
x = sorted(nums,reverse=True)
print(x[0],'is the greatest number in the list')

#Finding the smallest number form the list
y = sorted(nums)
print(y[0],'is the smallest number in the list')

#Finding the sum of all elements in the list
def sum_of_num(items):
    sum = 0
    for x in items:
        sum+=x
    return sum
result=sum_of_num(nums)
print(result)

#Finding the product of all elements in the list
def sum_of_num(items):
    sum = 1
    for x in items:
        sum*=x
    print(sum)
sum_of_num(nums)





