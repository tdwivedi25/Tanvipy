class Myclass():
    y = 2
    a = 5
    print(y+a)
    def method1(self):
        print('Hello World')
    def method2(self,string):
       print(string)
x=Myclass()
x.method1()
print(x.y)
print(x.a)
x.method2('Good Morning')

print()

z=Myclass()
z.method1()
print(z.y)
print(z.a)
z.method2('Good Morning')
