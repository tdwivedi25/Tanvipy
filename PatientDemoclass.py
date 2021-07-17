class Patient:

    def __init__(self):
        self.__id=34
        self.__name="Lincoln"
        self.__ssn="333444555"

    def setId(self,id):
        self.id=id

    def getId(self,id):
        return self.__id


    def setName(self,name):
        self.name=name

    def getName(self):
        return self.__name


    def setSSN(self, ssn):
        self.ssn = ssn

    def getSSN(self):
        return self.__ssn



P1 = Patient()

print(P1._Patient__id)
print(P1._Patient__name)
print(P1._Patient__ssn)





