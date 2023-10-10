from re import*
phone=(input("enter a number:"))
rule="\d{10}"
matcher=fullmatch(rule,phone)

if(matcher==None):
    print("invalid")
else:
   print("valid")