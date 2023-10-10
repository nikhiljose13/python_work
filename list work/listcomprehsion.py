lst=[2,3,4,5,6]
cube=[ n**3 for n in lst ]
print(cube)

sqaure=[n**3 for n in lst if n%2==0]
print(sqaure)

add_tow=[n+2 for n in lst]
print(add_tow)

gt_five=[n for n in lst if n>5]
print(gt_five)