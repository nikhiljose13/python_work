class moblie:
    model:str
    color:str
    brand:str
    price:int
    
    def __init__(self,model,color,brand,price,):
        self.model=model
        self.color=color
        self.brand=brand
        self.price=price
        
    def display(self):
        print(self.model,self.color,self.brand,self.price)
    
    def __str__(self) -> str:
        return self.model 

mob1=moblie("14 pro","black","apple",25000)

# mob1.display()
print(mob1)