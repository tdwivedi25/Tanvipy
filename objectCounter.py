class ObjectCounter:
    numberofObjects=0

    def __init__(self):
        ObjectCounter.numberofObjects+=1


    @staticmethod
    def displayCount():
          print(ObjectCounter.numberofObjects)

obj1=ObjectCounter()
obj2=ObjectCounter()
obj3=ObjectCounter()
ObjectCounter.displayCount()