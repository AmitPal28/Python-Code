#********************************************** Complex Number ***************************************************

# Directly use without math module
z = complex("1+2j")
print("Your Complex number is:", z)
print(type(z))

'''
# ValueError: complex() arg is a malformed string
z1 = complex(" 2 + 3j")
print("Your Complex number is:", z1)
'''


numOne = complex()
print("Your numOne Complex number is:",numOne)

numTwo = complex(6)
print("Your numTwo Complex number is:",numTwo)

numThree = complex("4")
print("Your numThree Complex number is:",numThree)

'''
 # TypeError: complex() can't take second arg if first is a string
numFour = complex("2","3")
print("Your numFour Complex number is:",numFour)

 # TypeError: complex() second arg can't be  a string
numFive = complex(2,"3")
print("Your numFour Complex number is:",numFive)

'''


''' ****************************************************************************************************************************
Concept of modulus : Modulus mean distance b/w polar coordinates and origin point.(  r=squrt( (real)**2 + (img)**2 )  )

Concept of phase of a complex number: the angle between the positive real axis and the vector representing a complex number. 
 
Concept of Polar: return(Modulus,Phaseangle)

Concept of Rectangular Coordinate:  It returns a value numerically equal to r * (math.cos(ph) + math.sin(ph)*1j)

*************************************************************************************************************************** ''' 

# Calculate Polar Coordinate, Modulus and Phase_angle
import cmath

def convert_to_polar(complex_num):
    # Convert the complex number to polar coordinates
    polar_num = cmath.polar(complex_num)
    # Extract modulus and phase angle from the polar representation
    modulus = polar_num[0]
    phase_angle = polar_num[1]
    return modulus, phase_angle

# Read the complex number as input
complex_input = complex(input("Enter a Complex Number is: ").strip())

# Convert the complex number to polar coordinates
modulus, phase_angle = convert_to_polar(complex_input)

# Print the results with three decimal places
print(f"Modulus of userComplex number is: {modulus:.3f}")
print(f"Phange Angle of userComplex number is: {phase_angle:.3f}")
