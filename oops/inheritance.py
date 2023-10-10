class parent:
    phone="iphone"
    vehicle="duke"

    def mobile(self):
        print(self.phone)
    def bike(self):
        print(self.vehicle)

class child(parent):
    pass

obj1=child()
obj1.mobile()
obj1.bike()