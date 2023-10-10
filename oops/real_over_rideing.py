class Parent:

    vechiles=["800","Honda Unicorn"]

    def properties(self):
        return self.vechiles

class Child(Parent):
    
    def properties(self):
        self.veh=super().properties()
        self.veh.append("BMW")
        return self.veh

obj=Child()
print(obj.properties())