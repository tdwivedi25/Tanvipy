from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):

    def scroll(self):
       print("Scrolling in HP")

class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling in Dell")

class HPNotebook(HP):
    def click(self):
        print("HP Notebook is clicking")

class DellNotebook(Dell):
    def click(self):
        print("Dell Notebook is clicking")



dell1=DellNotebook()
dell1.scroll()
dell1.click()


hp1=HPNotebook()
hp1.scroll()
hp1.click()

