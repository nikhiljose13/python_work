start=int(input("enter a range :"))
prev=0
current=1
print(prev)
print(current)
while(current<=start):
    sum=prev+current
    print(sum)
    prev=current
    current=sum
    start+=1