''' 
# Display Fibonacci series using loop
num= int(input("Enter a number you wants to obtained fibonacci series: "))
first=0
second=1

if num == 1:
    print(first)

else:
    print(f"Fibonacci Series till your entered value: {first}")
    print(f"Fibonacci Series till your entered value: {second}")
    for i in range(2,num):
        temp = first + second
        first= second
        second = temp
        print(f"Fibonacci Series till your entered value: {temp}")  '''


# Display fibonacci pattern using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("Enter a number you wants to obtained fibonacci series: "))
if num <= 0:
    print("Please Enter positive number:")
else:
    for patt in range(num):
        print(f"Pattern lies between b/w 1 to {num}: {fibonacci(patt)}")