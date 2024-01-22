#== Problem == Display Great Common Divisor or Highest Commom Factor between two numbers
def GCD(n1,n2):
    if n1 > n2:
        small = n2
    else:
        small = n1

    for i in range(1,small+1):
        if (n1%i == 0) and (n2%i == 0):
            hcf = i
    return hcf

n1= int(input("Enter first number: "))
n2= int(input("Enter second number: "))
print("The hcf of  two number",GCD(n1,n2))