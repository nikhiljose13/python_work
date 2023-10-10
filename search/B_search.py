lst=[10,23,45,67,21,55,66]
element=10
lst.sort()

low=0
upper=len(lst)-1

is_present=False
while(low<=upper):
    mid=(low+upper)//2
    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upper=mid-1
    elif element>lst[mid]:
        low=mid+1
print(is_present)

         
         
