height_incm=int(input("enter height in cm :"))
weight_inkg=int(input("enter weight in kg :"))

height_inm=(height_incm/100)

bmi=weight_inkg//height_inm**2

if(bmi<19):
    print("under weight")
elif(bmi<=19):
    print("normal weight")
elif(bmi<=25):
    print("over weight")
elif(bmi>30):
    print("obesity")
    


