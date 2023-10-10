#Abstraction = Hiding implimentation detailing..........

from abc import ABC,abstractmethod

# ------abstracted class-----------
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Ritz(Car):

    def start(self):
        print("Ritz starts")

    def accelerate(self):
        print("Ritz accelerate")
    
    def stop(self):
        print("Ritz stops")

obj=Ritz()
obj.start()
obj.accelerate()
obj.stop()
