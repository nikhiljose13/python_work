num=int(input("enter a number :"))
sum=0
while(num!=0):
    last_digit=num%10
    num=num//10
    sum+=last_digit
print(sum)
