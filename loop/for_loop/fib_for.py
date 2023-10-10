num=int(input("enter the number:"))
prev=0
current=1

print(prev)
print(current)

for i in range(1,num+1):
    sum=prev+current
    prev=current
    current=sum 
    if sum<=num:
     print(sum)
    else:
     break
