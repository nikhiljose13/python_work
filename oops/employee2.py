class employee:

    data=[
             {"id":1,"name":"jhon","dept":"hr","salary":34000},
             {"id":2,"name":"hari","dept":"it","salary":24000},
             {"id":3,"name":"ravi","dept":"qa","salary":64000},
             {"id":4,"name":"vijay","dept":"hr","salary":74000},
             {"id":5,"name":"tom","dept":"it","salary":24000},
             {"id":6,"name":"vipin","dept":"qa","salary":14000},
        
        ]
    def get(self,*args,**kwargs):   
        return self.data
    
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[emp for emp in self.data if emp.get("id")==id]
        return record
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[emp for emp in self.data if emp.get("id")==id].pop()
        self.data.remove(obj)

    def update(self,id=None,*args,**kwargs):
        id=id
        obj=[emp for emp in self.data if emp.get("id")==id].pop()
        obj.update(kwargs)
        print("employe object is updated")



obj=employee()

# print(obj.retrieve(id=2))

# obj.create(id=7,name="nikhil",dept="hr",salary=6000)

# obj.destroy(id=5)
obj.update(id=2,name="amal")
# print(obj.get())
print(obj.retrieve(id=2))