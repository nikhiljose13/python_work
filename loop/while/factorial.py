num=int(input("enter the number:"))

start=1
fact=1

while(start<=num):
    fact=fact*start
    start+=1
print(f"factorial of the number is {fact}")