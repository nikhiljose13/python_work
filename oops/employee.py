class employee:
    id:int
    name:str
    department:str
    gender:str
    salary:int

    def create(self,id,name,dept,gender,salary):
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender
        self.salary=salary
    def dispaly_emp(self):
        print(self.id,self.name,self.department,self.gender)

    def bouns(self,amount):
        self.salary+=amount
        print(f"the current salary after adding bouns {self.salary}")
    def prom(self,post):
        self.department=post
        print(f"{self.name} is promted to {self.department}")
    def __str__(self) -> str:
        return self.name
    
emp1=employee()
emp1.create(1001,"nikhil","hr","male",10000)
# emp1.dispaly_emp()
# emp1.bouns(300) 
emp1.prom("team lead")

print(emp1)