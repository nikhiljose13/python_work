lst=[3,5,6,2,1]
lst.sort()
if(lst[0]!=1):
    print("1 is missing")
else:
     for i in range(0,len(lst)):
          currrent=lst[i]
          next=lst[i+1]
          diff=next-currrent
          if diff!=1:
               print(currrent+1,"is missing")
               break
