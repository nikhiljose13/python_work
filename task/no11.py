count=int(input("number of people to be invited to the party:"))
if count<=10:
    for i in range(1,count+1):
       name=input("enter the names:")
    print(name," is invited")
else:
    print("to high")