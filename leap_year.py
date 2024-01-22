#== Problem == Enter  user enter year is leap year or not

num=int(input("Enter a year: "))
if (num % 400 == 0) and  (num % 100 ==0):
    print(f"Enter year:{num} is leap year.")
elif (num % 4 == 0) and (num % 100 != 0):
    print(f"Enter year:{num} is leap year.")
else:
    print(f"{num} is not leap year.")