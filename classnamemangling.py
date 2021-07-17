class Student:

    def __init__(self):
        self.__id=23
        self.__name="SD"

    def display(self):
        print(self.__id)
        print(self.__name)

s1=Student()
#s1.display()
print(s1._Student__id)
print(s1._Student__name)