#multilevel inheritance

class Parent():
    def method1(self):
        print("Nokia")

class Child(Parent):
    def method1(self):
        print("Redme")

    def method2(self):
         print("Apple")


class Child1(Child):
    def method3(self):
        print("Apple10")

#c1=Child()
#c1.method1()
#
#c2=Child1()
#c2.method1()

#multiple level inheritance

class P1():
    def method1(self):
        print("Nokia")

class P2():
    def method1(self):
        print("Redme")

    def method2(self):
         print("Apple")

class C1(P1,P2):
    def method3(self):
        print("Apple10")


obj1=C1()
obj1.method1()
