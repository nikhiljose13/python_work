from datetime import datetime
class Bank:
    bank_name:str
    accno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,p_name,acc_no,ac_type,bal):
        self.bank_name=b_name
        self.accno=acc_no
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance += amount
        print(f"  Your{self.bank_name}has been credited with {amount} Available Balance is{self.balance}")

    def withdrawl(self,amount):
        if amount < self.balance:
            self.balance-=amount
            print(f" Your {self.bank_name} account has been debited with {amount}. Available Balance is {self.balance}\n")

        else:
            print("\nInsufficent Fund....... :(\n")
    def balance_(self):
        print(f"\n Your {self.bank_name} account of Account Number {self.accno} has balance of {self.balance} in {datetime.today()} \n")

obj1=Bank()
obj1.create("sbi","1001","nik","sav",6000)
obj1.deposit(500)

obj2=Bank()
obj2.create("sbi","1002","nikhil","sav",5000)
obj2.withdrawl(3000)
obj2.balance_()