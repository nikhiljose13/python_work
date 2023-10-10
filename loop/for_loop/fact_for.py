num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    i+=1
print(f"factorial of the number is ={fact}")