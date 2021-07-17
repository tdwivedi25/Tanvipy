#Method Overloading
class DrivingClass:
 def data(self,name=None,age=None):
  if name==None and age == None :
      print("You dont want a driver's",'license.')
  elif name!= None and age<18:
      print(name,'is not eligible for a driver','license.')
  elif  name!= None and age>=18:
      print(name, 'is  eligible for a driver', 'license.')

Tanvi=DrivingClass()
Pankaj=DrivingClass()
Shalini=DrivingClass()
Tanvi.data()
Pankaj.data('Pankaj',42)
Shalini.data('Shalini',39)

#Method Overriding
class Parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print('I am a parent and my name is',self.name,'.')

class Child(Parent):

    def display(self):
      super().display()
      print('I am a child and my name is', self.name, '.')

obj1=Child('xyz')
obj1.display()




