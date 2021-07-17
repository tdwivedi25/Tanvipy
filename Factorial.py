#Creating  factorial of a number

import re
def fact(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

y=int(input("Enter your number to find its factorial :"))
result=fact(y)
print(result)

def fact1(n):
    if n==0:
        return 1
    return n* fact1(n-1)

y1=int(input("Enter your number to find its factorial :"))
result=fact(y1)
print(result)


str1="Sha-lini"

list1=[]
for i in str1:
    list1.append(i)
print(list1)

for i in range(len(list1)-1,-1,-1):
    print(list1[i],end="")
print()

strnew=re.findall(r"[A-Z]+[a-z]+-[a-z]+",str1)
print(strnew)

