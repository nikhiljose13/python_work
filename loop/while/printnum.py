start=1
end=45
while(start<=end):
    if(start%15==0):
      print("efg")
    elif(start%5==0):
       print("cd")
    elif(start%3==0):
       print("a")
    else:
       print(start)
    start+=1
    