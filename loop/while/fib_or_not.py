prev=0
current=1
start=1
num=int(input("enter a number:"))
# print(prev)
# print(current)
flag=False
while(start<=num):
    sum=prev+current
    # print(sum)
    prev=current
    current=sum
    if(sum==num):
        flag=True
        break
    start+=1
print(flag)
    
    