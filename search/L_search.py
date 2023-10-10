lst=[10,23,45,67,21,55,66]
element=21
i=0
limit=len(lst)

is_present=False

while(i<limit):
    cur_val=lst[i]
    if cur_val==element:
        is_present=True
        break
    i+=1
print(is_present)