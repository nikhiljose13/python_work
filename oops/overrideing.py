class bike:
    def start(self):
        print("kick")
    def breaking(self):
        print("drum")

class hero(bike):
    def start(self):
        print("self")
    def breaking(self):
        print("abs")
obj1=hero()

obj1.breaking()