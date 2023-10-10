def multiple(*args):
    res=1
    for num in args:
        res*=num
    return res
print(multiple(2,3,4))
