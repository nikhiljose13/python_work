# start with alp k,m,l
# second place must be digit dev by 3
#  followed by any char or digit
from re import*
variable=input("enter a variable:")

rule="[kml][369][\w]*"

matcher=fullmatch(rule,variable)

print("invalid" if matcher==None else "valid")