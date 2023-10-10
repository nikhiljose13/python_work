def largest(a,b,c):
   if  a>b and a>c:
    print(a, "is largest")
   elif b>a and b>c:
    print(b ,"is largest")
   else :
    print(c, "is largest")

a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
largest(a,b,c)