'''
#Problem Solving Skills:
-----------------------------------------------------------------------------
#== Problem-1 == How to work print function and escape character
print('Hi fresher\n How to feel while learning \"Python\" ?')
------------------------------------------------------------------------------
#== Problem-2 == Display Swapping two numbers without using three number
num1=int(input("Enter first number:"))
num2=int(input("Enter Second number:"))
num1, num2 = num2,num1
print("After Swapping first number is:",num1)
print("After Swapping second number is:",num2)

'''
num1= num1+ num2
num2= num1-num2
num1= num1-num2
'''
-------------------------------------------------------------------------------

#== Problem-3 == Average of three number user take numbers in a single line 
n1, n2, n3 = input("Enter a  three number separated by commas: ").split(",")
avg= (int(n1) +int(n2) +int(n3))/3
print(f"User Three numbers of average is {avg}")
-------------------------------------------------------------------------------

#== Problem-4 == Display area of triangle 
length= int(input("Enter a length of triangle:"))
width=int(input("Enter a width of triangle:"))
area= (0.5)*length*width
print(f"Area of triangle is: {area}")
------------------------------------------------------------------------------
#== Problem-5 == Display area of a circle using 'math' module
import math
radius =  float(input("Enter user radii: "))
area = math.pi * (radius**2)
print(f"Area of a circle is: {area}") 
--------------------------------------------------------------------------------
#== Problem-6 == Display Square root of a number using 'math' module
import math
num=int(input("Enter a number: "))
sq_num= math.sqrt(num)
print(f"Enter number is: {num} and its square-root is: {sq_num} ")
--------------------------------------------------------------------------------
#== Problem-7 == Display random number for a particular range
import random
num= random.randint(50,100)
print(f"Random number between 50 and 100 is: {num}")
-------------------------------------------------------------------------------

#== Problem-8 == Convert into kms to miles
kms=int(input("Enter your distance cover in kilometer: "))
miles= 0.6 * kms
print(f"Distance reached in {kms} kms will be {miles} miles.")
------------------------------------------------------------------------------

#== Problem-9 == Convert into celsius to fahrenheit
celsius= int(input("Enter a Celsius Value:"))
faherenheit= (celsius*(5/9)+ 32)
print(f"Celsius:{celsius} will be {faherenheit} Faherenheit.")
------------------------------------------------------------------------------
#== Problem-10 == Display input number is positive, negative or zero
num=int(input("Enter a number:"))
if num <0:
    print("Enter number is \"Negative\"")
elif num == 0:
    print("Enter number is \"Zero\"")
else:
    print("Enter number is \"Positive\"")
------------------------------------------------------------------------------
#== Problem-11 == Sum of n natural number
num= int(input("Enter natural number: "))
sum=0
i=1
while(i<=num):
    sum +=i
    i +=1
print(f"Sum of user enter natural number is {sum}")
-------------------------------------------------------------------------------
#== Problem-12 == Display User input number is even or odd 
num = int(input("Enter a number :"))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is Odd number")
----------------------------------------------------------------------------------
#== Problem-13 == Display number is  prime or not
num = int(input("Enter number: "))
if num == 1:
    print(f"{num} is not a prime")
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime ")
-----------------------------------------------------------------------------------------
#== Problem-14 == Display ASCII Value of each character in a user string
number = input("Enter a string: ")
for i in number:
    print(f"Ascii values of {i} : {ord(i)}")
------------------------------------------------------------------------------------------
#== Problem-15 == Reverse string using slicing
user_name=input("Enter your string: ")
print(f"reverse name of user is: {user_name[-1::-1]}")
-----------------------------------------------------------------------------------------
#== Problem-16 == Random take wining number is match with user guess number
import random
winining_num= random.randint(10,20)
print(f"winning number is: {winining_num} ")
for num in range(0,winining_num): 
    guess_num= int(input("Enter a guess number: "))
    if guess_num == winining_num and num < winining_num:
        print("Your guess number is correct")
        break
    elif guess_num < winining_num and num < winining_num:
        print("Your guess number is low")
    else:
        print("Your guess number is high")

    if num <= winining_num-1:
        print("Last Attempt:")
---------------------------------------------------------------------------------------
#== Problem-17 == User_name start with 'a' or 'A' and age above 10 then watch show 
user_name  = input("Enter a user name: ")
user_age = int(input("Enter user age: "))

if user_name[0] == 'a' or user_name[0]== 'A' and user_age>10:
    print("You can watch show now")
else:
    print("Sorry, you can not watch show")

#== Problem-18 == Count individual character not repeated one in an user take string 
full_name= input("Enter user Full name:")
i=0
temp_var=""
while(i< len(full_name)):
    if full_name[i] not in temp_var:
        temp_var += full_name[i] 
        print(f"{full_name[i]}: {full_name.count(full_name[i])}")
    i +=1


'''