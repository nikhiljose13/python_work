name=input("enter a name:")
number=int(input("enter a number:"))
if number<10:
    for i in range(1,number+1):
        print(name)
else:
    print("to high")