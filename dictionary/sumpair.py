lst=[2,3,5,6,4,7]
sum=10
# total=8
#  sum=0
# for i in lst:
#     for e in lst:
#         sum=i+e
#         if sum==total:         
#           print(i,e)
lst.sort()

low=0
upper=len(lst)-1
while(low<upper):
    cur_sum=lst[low]+lst[upper]
    if cur_sum==sum:
        print("pairs:",lst[low],lst[upper])
        break
    elif cur_sum<sum:
        low+=1
    else:
        upper-=1