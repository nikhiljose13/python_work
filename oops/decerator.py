class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @property
    def get_name(self):
        return self.name
    
obj=student("hari",35)
print(obj.get_name)
print(obj.age)
        