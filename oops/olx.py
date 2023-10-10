class olx:
    vehicles=[
            {"id":1,"name":"passionpro","year":2010,"selling_price":34000,"color":"black","location":"ekm"},
            {"id":2,"name":"cbz","year":2015,"selling_price":28000,"color":"red","location":"tsr"},
            {"id":3,"name":"alto","year":2000,"selling_price":100000,"color":"silver","location":"tsr"},
            {"id":4,"name":"reclassic350","year":2018,"selling_price":120000,"color":"grey","location":"ekm"},       
            {"id":5,"name":"activa","year":2010,"selling_price":24000,"color":"black","location":"ekm"},
            {"id":6,"name":"herohondasd","year":2000,"selling_price":80000,"color":"red","location":"tsr"}
            ]
    
    def create(self,*args,**kwargs):
        self.vehicles.append(kwargs)
        return kwargs

    def get(self,*args,**kwargs):   
        return self.vehicles
    
    def update(self,id=None,*args,**kwargs):
        id=id
        obj=[vh for vh in self.vehicles if vh.get("id")==id].pop()
        obj.update(kwargs)
        print("vehicles object is updated")

    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[vh for vh in self.vehicles if vh.get("id")==id]
        return record
    
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[vh for vh in self.vehicles if vh.get("id")==id].pop()
        self.vehicles.remove(obj)


obj=olx()

# print(obj.create(id=7,name="ktm",year=2018,selling_price=80000,color="red",location="tsr"))

# obj.destroy(id=2)
# print(obj.get())
print(obj.retrieve(id=3))