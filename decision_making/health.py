tummy_size=int(input("enter the tummy size :"))
buttock_size=int(input("enter the buttock size :"))
gender=input("enter the gender:")
measurement=tummy_size/buttock_size 
val=round(measurement,2)
if gender=="male":
    if(val<0.95):
        print("health risk low \nbodyshape pear")
    elif(val<1.0):
        print("health risk modrate \nbody shape avocado")
    else:
        print("health risk high body shape apple")
elif  gender=="female":
    if(val<0.80):
        print("health risk low \nbodyshape pear")
    elif(val<0.85):
        print("health risk modrate \nbody shape avocado")
    else:
        print("health risk high body shape apple")
else:
    print("invalid gender")

#  print(f"measurement")