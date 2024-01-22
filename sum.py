'''
a=int(input())
b=int(input())
sum=a+b
print(sum)
'''
# User input take and display the sum of two number using fn.
def add(a,b):
    sum= a+b
    return sum
a=int(input("Enter first:"))
b=int(input("Enter Second:"))
result= add(a,b)
print(f"The Addition of two numbers {result}")
