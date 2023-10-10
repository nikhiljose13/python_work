start=10
stop=50

for num in range(start,stop+1):
    is_prime=True
    for n in range(2,num):
        if num%n==0:
            is_prime=False
            break
    if(is_prime==True):
        print(num)
