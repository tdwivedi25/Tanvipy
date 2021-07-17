try:
   UserPwd=input("Enter a password: ")
   assert len(UserPwd)>=8, "Password is less than 8 chracters"
except AssertionError as obj:
    print(obj)
    print("try again")
else:
  print("Password entered successfully")


x=16
print(hex(16))
print(bin(x))
print(oct(x))
print(id(x))

x="sd"
print(x)

friendly=False
if friendly:
    greeting="Hello World"
else:
    greeting=12*12
print(greeting)

a="sd"
b=a
print(id(a),id(b))
b="_shalini"

print(id(a),id(b))


g="Call int(x, base) with base as 16 to convert the hexadecimal string x to an integer.\
 Use bin(number) with the resulting integer as number to convert it to a binary string."
print(g)

_x="23"
print(_x*3)
print(_x[0])



str1="Isn\'t it"
str2=r"First Line.\tSecond Line."
print(str1)
print(str2)

str3=str2.replace("F","Th")
print(str3)
print(str2.split(" "))
print("Hello World"+str(1))
print(10/3)
print(.9//.3)


#ternary operators max (a>b>?a:b in C

p=34
q=21
max=p if p>q else q
print(max)


i=1
for i in range(1, 10):
    if i<5:
        print(str(i)+" is less than 5")
    elif i == 5:
            print(str(i) + " is equal to 5")
    else:
            print(str(i) + " is greater than 5")


a=1
while a<=6:
    if a%5==0:
        continue

    print(a)
    a+=1


for x in 'Amazon':
    if x == 'z':
        break
    print(x)