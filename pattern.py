'''
#**************************************** Problem1 *******************************************************************************
# Replace all __ with rjust, ljust or center.
thickness = int(input()) #This must be an odd number c = 'H'
c= 'H'
# Top Cone
for i in range(thickness): print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2): print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness): print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

'''

'''
#******************************************* Problem2 ***********************************************************
# Read the size of the mat (X) and the number of columns (M) separated by a space
X, M = map(int, input().split())

# Top part of the mat
for i in range(1, X, 2):
    print(('.|.' * i).center(M, '-'))

# Welcome message
print('WELCOME'.center(M, '-'))

# Bottom part of the mat
for i in range(X-2, -1, -2):
    print(('.|.' * i).center(M, '-'))

'''

'''
#******************************************* Problem3 ********************************************************
def print_rangoli(size):
    import string

    # Generate the alphabet
    alphabet = string.ascii_lowercase

    # Create the lines of the rangoli
    lines = []
    for i in range(size):
        # Generate the sequence of alphabets for each line
        seq = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        # Add the line to the list of lines
        lines.append((seq).center(4*size-3, '-'))

    # Print the top half of the rangoli
    print('\n'.join(lines[:0:-1] + lines))

# Read the size of the rangoli from input
userSize = int(input("Enter the size of rangoli :"))

# Call the function to print the rangoli
print_rangoli(userSize)
'''

