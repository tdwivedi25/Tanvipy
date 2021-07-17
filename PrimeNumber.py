num = int(input("Enter an integer: "))
for x in range(2,num):
    if num%x==0:
       print("Not prime")

       break


else :
    print("It is a prime number.")



