low_limit=int(input("lower limit:"))
up_limit=int(input("upper limit:"))
total=0
for i in range(low_limit,up_limit+1,+1):
    total=total+low_limit
    low_limit+=1  
print(total)