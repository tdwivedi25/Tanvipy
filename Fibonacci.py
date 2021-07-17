import math

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for x in range(n):
        c=a+b
        a=b
        b=c
        print(c)

fib(5)
## using temp variable for swap
#a=1
#b=6
#print("befor swap:", a,b)
#temp=a
#a=b
#b=temp
#print("After swap:", a,b)
#
## without using temp variable
#a=a+b
#b=a-b
#a=a-b
#print("After swap:",a, b)
#
## using XOR for swap
#a=a^b
#b=a^b
#a=a^b
#print("After swap:",a, b)
#
#binlist=[]
#for i in range(1,11):
#     binlist.append(bin(i).replace("0b",""))
#print(binlist)
#
#
#
#n=int(input("enter your number:"))
#for i in range(2,n):
#    if n%2==0:
#        print("not prime")
#        break
#else:
#        print("prime")
#
#
#numlist=[]

#for i in range(1, 101):
#    if i%3==0 or i%5==0:
#       continue
#    else:
#        print(i)
#print("bye")
#
#
#print(4**(.5))
#print(int(4**(.5)))
#
#for i in range(1,51):
#    if (i ** (.5) == int(i ** (.5))):
#        print(i, end=" ")
#
#for i in range(1,51):
#   if (math.sqrt(i) == i**(.5)):
#        print(i, end=" ")