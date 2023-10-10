from re import*
num_plate=input("enter a variable:")

rule="(kl)\d{2}[a-z]{1,2}\d{4}"

matcher=fullmatch(rule,num_plate)

print("valid" if matcher!=None else "invalid")