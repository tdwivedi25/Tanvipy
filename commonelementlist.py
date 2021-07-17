a=[1,3,4,6]
b=[3,7,8,9,1]
res=[]
for i in a:
    if i in b:
        res.append(i)
print(res)


res=[i for i in a if i in b]
print(res)


class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def avg(self):
         numberofratings=len(self.ratings)
         average= sum(self.ratings)/numberofratings
         print("Average of ratings for",self.name,"is",average)
    def setName(self, name1):
        self.name1=name1
    def getName(self):
        return self.name1

    def display(self):
        print(self.name)
        print(self.ratings)

c1=Course("SD",[3,4,5])
print(c1.name, c1.ratings)
c1.avg()
c1.display()
c1.setName("Shalini")
res=c1.getName()
print(res)

