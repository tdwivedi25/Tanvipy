l1 = [x for x in input("enter series of numbers:").split(",")]
print(l1)
l1.append(23)
print(l1)
l1.insert(2,"sd")
print(l1)
l1.remove('sd')
print(l1)


math=int(input("enter your maths marks out of 100:  "))
physics=int(input("enter your physics marks out of 100:  "))
chemistry=int(input("enter your chemistry marks out of 100:  "))
if math>=35 and physics>=35 and chemistry>=35:
    print("you passed the exam")
else:
    print("you failed")

averagemarks=(math+physics+chemistry)/3
print("your average marks is :", averagemarks)
if averagemarks<=59:
    print("your grade is C")
elif averagemarks<=69:
    print("your grade is B")
else:
    print("your grade is A")



list1=[3,4,5,6,7]
newlist=list(map(lambda x:x**3, list1))
print(newlist)


lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)

lsteven=[]
lsteven=[x for x in range(1,25) if x%2==0]
print(lsteven)


a=[2,3,4,5]
b=[5,6,7,8,10]
z=[]
for i in range(len(a)):
      z.append(a[i]*b[i])
print(z)

z1=[a[i]*b[i] for i in range(len(a))]
print(z1)

c=[int(x) for x in input("enter numbers:").split(",")]
print(c)

d=[int(x) for x in input("enter numbers:").split(",")]
print(d)



