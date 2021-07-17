c=100
def myfunc(*b):
    #global c
    c=0
    #d=globals()['c']
    globals()['c']=0
    for i in b:
        c=c+i
    print("Sum is :", c)
print("global value of c is: ", c)
def student(name, age=18):
    print("name is :", name)
    print("Age is :", age-5)

def employee(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
    #print(data)

lst=[]
for i in range(10):
    c=45
    lst.append(c)
    c+=1

print(lst)

print(max(lst))
print(sin(lst))



myfunc(11,22,44,55,66)
student("Tanvi",20)
employee("Shalini", age=20,Mob=981076,Country="United States")



