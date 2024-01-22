#Display Armstrong number or not 
number= int(input("Enter a number for check armstrong: "))
order= len(str(number))
sum=0
temp=number
for i in range(order):
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == number:
    print(f"Yes,Your entered number {number} is Armstrong")
else:
    print(f"No,Your entered number {number} is not Armstrong")

''' 
#Armstrong number for lying particular interval
lower=int(input("Enter a lower limit: "))
upper=int(input("Enter a upper limit: "))

for number in range(lower,upper+1):
    order= len(str(number))
    sum= 0
    temp= number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        print("Interval lies b/w {lower} and {upper}: ", number )
'''