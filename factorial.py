'''
#Factorial number using loop
num=int(input("Enter a  number:"))
fact=1
for i in range(1,num+1):
    fact= fact*i
print(f"Factorial number is",fact)
'''

# factorial number using recursion
def factorial(n):
    if n < 0:
        print("factorial below zero doesn't exist")
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a number whose factorial you want: "))
result= factorial(num)
print(f"Factorial of {num} is {result}")