# 1st 3 char any random upper case
# 4th p,f,a,c,h,t
# 5th upper case random alp
# 4 digit
# in last pos one random alphapet
from re import*
pan_id=input("enter a variable:")

rule="[A-Z]{3}[PFACTH][A-Z][\d{4}][a-z]"

matcher=fullmatch(rule,pan_id)

print("invalid" if matcher==None else "valid")