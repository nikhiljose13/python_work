# Python code to swap two numbers
# without using another variable


x = (input("enter anumber:"))
y = (input("enter anumber:"))

print ("Before swapping: ")
print(f"Value of x={x} Value of y={y}")

# code to swap 'x' and 'y'
x, y = y, x

print ("After swapping: ")
print(f"Value of x :{x} and y : {y}")
