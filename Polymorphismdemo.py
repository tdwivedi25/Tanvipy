class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hello")

def calltalk(obj):
    obj.talk()

d1=Duck()
calltalk(d1)

h1=Human()
calltalk(h1)