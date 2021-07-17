#using arithematic operators
class Compute:
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __mul__(self, other):
         return self.num * other.num
    def __truediv__(self, other):
         return self.num/ other.num
    def __floordiv__(self, other):
         return self.num// other.num
    def __mod__(self, other):
        return self.num % other.num
    def __pow__(self, other):
        return self.num ** other.num

obj1=Compute(5)
obj2=Compute(4)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1//obj2)
print(obj1 % obj2)
print(obj1 ** obj2)


