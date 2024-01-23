'''
#list Practice Problem:
-------------------------------------------------------------------------------------
#== Problem-1 == Display given list element of a square  create a random  b/w 0 to 7 
def square_num(n):  #where n is a list items
    n_l=[]
    for num in n:
        n_l.append(num**2) 
    return n_l
l=list(range(0,8))
print(f"Square of given list element is: {square_num(l)}")
---------------------------------------------------------------------------------------
#== Problem-2 == Display given list converts into reverse list  
def reverse_list(n):
    n_l=[]
    for i in n[::-1]:
        n_l.append(i)   
    return n_l

l=[3,6,4,7]
print(f"Reverse of a given list element is: {reverse_list(l)}")
------------------------------------------------------------------------------------------
#== Problem-3 == Display reverse of character inside element in a list
def rev_list_element_indi(n):
    n_l=[]
    for i in n:
        n_l.append(i[::-1])
    return n_l
l=["Shivani","Kajal","Neetu"]
print(f"Character inside list element reverse is :{rev_list_element_indi(l)}")
-------------------------------------------------------------------------------------------
#== Problem-4 == Display combination between two list 
def even_odd_inside_list(l):
    l1=[]
    l2=[]
    for i in l:
        if i%2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    combine = [l1,l2]
    return combine

numbers=list(range(1,11))
print(f"Combination of odd list and even list of an other list is:{even_odd_inside_list(numbers)}")
----------------------------------------------------------------------------------------------------
#== Problem-5 == Display commmon element between  two list 
def common_element(l1,l2):
    cmn_ele=[]
    for i in l1:
        if i in l2:
            cmn_ele.append(i)
    return cmn_ele

num1=['Neetu','Kajal','Bhagya','Anushka','Priya']
num2=['Neetu','Geetanjali','Shivani','Kajal']
print(f" Common elements of given two list is: {common_element(num1,num2)}")
------------------------------------------------------------------------------------------------------
#== Problem-6 == Find Highest element of a user take list 
user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
first= user_list[0]

for i in range(1,len(user_list)):
    if user_list[i]>first:
        first = user_list[i]
        print(f"Higest Value element in a list:{first}")
----------------------------------------------------------------------------------------------------------
#== Problem-7 == Find Smallest element of a user take list
user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
first= user_list[0]

for i in range(0,len(user_list)):
    if user_list[i]<first:
        first = user_list[i]
        print(f"Smaller Value element in a list:{first}")
----------------------------------------------------------------------------------------------------------
#== Problem-8 == Find Second Highest element of a user take list
def sec_high(input_list):

    if len(input_list) < 2:
        return "List must have at least two elements"

    first= max(input_list[0],input_list[1])
    second= min(input_list[0],input_list[1])
    for i in input_list[2:]:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i

    return second

user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
result = sec_high(user_list)
print("Second-highest element:", result)
---------------------------------------------------------------------------------------------------------
#== Problem-9 == Find Second Lowest element of a user take list
def second_lowest(input_list):
    if len(input_list) < 2:
        return "List must have at least two elements"

    lowest = min(input_list[0], input_list[1])
    second_lowest = max(input_list[0], input_list[1])

    for i in input_list[2:]:
        if i < lowest:
            second_lowest = lowest
            lowest = i
        elif i < second_lowest and i != lowest:
            second_lowest = i

    return second_lowest

user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
result = second_lowest(user_list)
print("Second-lowest element:", result)

'''