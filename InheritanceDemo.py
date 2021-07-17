from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self, make, model, year):
            self.make=make
            self.model=model
            self.year=year

    def start(self):
        print("starting the car")

    def stop(self):
        print("stopping the car")

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

     def __init__(self, cruiseControlEnabled, make, model, year):
              BMW.__init__(self, make, model, year)
              self.cruiseControlEnabled=cruiseControlEnabled

     def start(self):
         super().start()

     def stop(self):
         print("button stopping the car")

     def drive(self):
         print("driving 1")
class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        #BMW.__init__(self, make, model, year)
        super().__init__(make,model,year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
        print("driving 2")
threeSeries=ThreeSeries(True, "BMU", "328i", "2018")

print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.drive()

FiveSeries=FiveSeries(True, "Noka", "890", "2019")
print(FiveSeries.year)
FiveSeries.start()
FiveSeries.stop()
FiveSeries.drive()