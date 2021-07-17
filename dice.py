import random

while True:
    rolled_num = random.randint(1,6)
    print("The dice rolled and you got: ", rolled_num)
    input("Press any key to roll again.")
    break


sum=lambda arg1, arg2:arg1+arg2

print("Sum of nos. is: ", sum(2,3))
print("Sum of nos. is: ", sum(12,13))
