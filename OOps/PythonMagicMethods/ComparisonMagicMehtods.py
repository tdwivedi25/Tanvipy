class Comparison:
    def __init__(self,num):
        self.num=num
    def __lt__(self, other):
        return self.num < other.num
    def __gt__(self, other):
        return self.num > other.num
    def __le__(self, other):
        return self.num <= other.num
    def __ge__(self, other):
        return self.num >= other.num
    def __ne__(self, other):
        return self.num != other.num
    def __eq__(self, other):
        return self.num == other.num

obj1=Comparison(8)
obj2=Comparison(16)
print(obj1<obj2)
print(obj1>obj2)
print(obj1<=obj2)
print(obj1>=obj2)
print(obj1!=obj2)
print(obj1==obj2)


