expenses=[11500,40000,50000,34000,200,500000]
min_exp=expenses[0]
for e in expenses:
    if e<min_exp:
        min_exp=e
print(min_exp)
total=sum(expenses)
print(total)