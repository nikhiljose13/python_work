number=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for n in number:
    even.append(n) if n%2==0 else odd.append(n)
print(odd)
print(even)