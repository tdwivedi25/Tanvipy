a = 45
print(oct(a))

for i in range(2, 90):
    print(bin(i))

s1 = """
      You are the 
      creater
      of your destiny
   """



x = int(input("Enter the number: "))

for i in range(1, x + 1):
    if i % 10 == 0:
        continue
    if i >100:
        break
    print(i)


primeflag=True

n=int(input("Enter your number to test if it is prime or not: "))
for i in range(2, n):
    if n%i==0:
        primeflag=False
if (primeflag):
        print("prime number")
else:
        print("not a prime number")


def customgen(x,y):
    while x<y:
        yield x
        x+=1
result=customgen(10,20)

for i in result:
    print(i)

