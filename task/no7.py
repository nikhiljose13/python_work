num=int(input("enter a number:"))
n=0
for i in range(1,(10+1)):
    multiple=num*i
    i+=1
    n+=1
    print(f"{num}*{n}=",multiple)