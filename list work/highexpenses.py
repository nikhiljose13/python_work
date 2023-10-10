expenses=[11500,40000,50000,34000,20000,22000]
max_exp=0

for e in expenses:
    if e>max_exp:
        max_exp=e
print(max_exp)