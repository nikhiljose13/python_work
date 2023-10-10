num=int(input("enter a number:"))
digit_count=len(str(num))
original=num
sum=0
while(num!=0):
    las_digit=num%10
    cube=las_digit**digit_count
    sum=sum+cube
    num=num//10

if(original==sum):
    print(f"{sum} is amstrong number")
else:
    print(f"{sum} not amstrong")