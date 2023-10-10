#Abstraction = Hiding implimentation detailing..........

from abc import ABC,abstractmethod

# ------abstracted class-----------
class Banking_App(ABC):
    @abstractmethod
    def fundtransfer(self):
        pass
    @abstractmethod
    def balance(self):
        pass
    @abstractmethod
    def history(self):
        pass

class PhonePe(Banking_App):

    def fundtransfer(self):
        print("PhonePe has the feature of transfer money ......")

    def balance(self):
        print("PhonePe has the feature to show your balance.....")
    
    def history(self):
        print("PhonePe has the feature to show your transfer History..... ")

class Gpay(Banking_App):

    def fundtransfer(self):
        print("Gpay has the feature of transfer money ......")

    def balance(self):
        print("Gpay has the feature to show your balance.....")
    
    def history(self):
        print("Gpay has the feature to show your transfer History..... ")

pp=PhonePe()
pp.fundtransfer()
pp.balance()
pp.history()

gp=Gpay()
gp.fundtransfer()
gp.balance()


