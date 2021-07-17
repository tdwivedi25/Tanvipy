class Mobile:
    len1=80
    len1.bit_length()
    print(type(len1))
    bdt=40

    def __init__(self, a, b):
        print("Initiated")
        self.a = a
        self.b = b


    def app(self):
        print("My new design: ", self.a,self.b)

mob1 = Mobile("New",15)
mob2 = Mobile("Old",16)

print(type(mob1))


print("My mobile length is: ", mob1.len1)
print("My mobile breadth is: ", mob2.bdt)
mob1.app()
mob2.app()


