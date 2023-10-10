# n1=int(input("enter a number:"))
# n2=int(input("enter a number:"))
# res=n1-n2 if n1>n2 else n2-n1
# print(res)

year=int(input("enter a year:"))
res="leap year" if (year%4==0 and year%100!=0) else "not leap year" if (year%400==0 and year%100==0) else "not leap year"
print(res)