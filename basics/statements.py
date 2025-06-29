import math

# Python Shell
"""
Try using python shell
"""


# Type Conversion

#Implicit Type Conversion
"""
 Implicit Type Conversion  - automatically done by the python intepreter
 E.g int to float
"""
distance = 250
print("Distance before implicit conversion =",distance)
distance = 252.5
print("Distance after implicit conversion = ",distance)


# Explicit Type Conversion

"""
Explicit Type Conversion - done by the programmer
"""

grade1 = float(input("Grade1: "))
grade2 = float(input("Grade2: "))
grade3 = float(input("Grade3: "))

avg = (grade1 + grade2 + grade3) / 3
print("Average grade (float) = ",avg)
print("Average grade (int) = ", int(avg))

ounces = int(input("Input ounces of water: "))
cups_drank = ounces / 8
cups_left = int( 8 - cups_drank)
print("Cups drank =", cups_drank, "and cups left", cups_left)

int_1 = input("Input the first integer: ")
int_2 = input("Input the second integer: ")

pdt = int(int_1)*int(int_2)
print("Pdt of the 2 integers =", float(pdt))

# Mixed data types
"""
E.g combining a float and integer produces a float
"""
quantity = input("Enter quantity: ")
price = input("Enter price: ")
total = int(quantity) * float(price)
print("Total = ", total)

"""
Combining numeric types and strings
input() - captures a string and so if input is meant to be a number,
it should be converted to a number before it is used in a calculation

"""

# * also serves as a repetition operator
print("Dallington " * 3)

num = int(input("Enter a number: "))
digits_str = input("Enter digits: ")
result = str(num) + "." + digits_str
print("Result:", result)

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
count = int(input("Enter count: "))

combined_str = str1 + " " + str2 + "\n"
print(combined_str * count)

# Floating point errors

# Print floats with 30 decimal places
print(f"{0.1:.30f}")

"""
A round-off error occurs when floating-point values are stored erroneously as an approximation. The
difference between an approximation of a value used in computation and the correct (true) value is called a
round-off error.

"""

# An overflow error occurs when a value is too large to be stored. The maximum and minimum floating-point
# print(f"{120.0**350}")

# round off function
print(round(3.145662, 3))

# Round off
base = float(input("Enter breadth: "))
height = float(input("Enter height: "))
area = 0.5 * base * height

print("Area of the triangle is ", round(area, 1))
print("Area of the triangle is ", round(area))


# Dividing Integers


"""
1. True division (/) converts numbers to floats before dividing.
   Ex: 7 / 4 becomes 7.0 / 4.0, resulting in 1.75.
2. Floor division (//) computes the quotient, or the number of times divided. 
   Ex: 7 // 4 is 1 because 4 goes into 7 one time, remainder 
3. The modulo operator (%) computes the remainder. 
   Ex: 7 % 4 is 3.
"""

print("7 / 4 =", 7 / 4)
print("7 // 4 =", 7 // 4)
print("7 % 4 =", 7 % 4)


# Unit Conversions

# Ex:1

hour = int(input("Enter Hour: "))
minute = int(input("Enter Minute: "))
add = int(input("Enter Add: "))

total_min = hour * 60 + minute + add
arrival_hour = total_min // 60 % 24
arrival_minute = total_min % 60

print("Arrival hour: ", arrival_hour, "Arrival minute: ", arrival_minute)


# Ex: 2

total_amount = float(input("Total Amount? "))
cash_payment = int(input("Cash payment? "))

change = round(cash_payment - total_amount, 2)
print("Change due: $", )

print()
print("Change due $", change)
change = int(change * 100)

# Print the results.
print()
print("  Dollars:", change // 100)
change = change % 100
print(" Quarters:", change // 25)
change = change % 25
print("    Dimes:", change // 10)
change = change % 10
print("  Nickels:", change // 5)
change = change % 5
print("  Pennies:", change)


# Math library
print("The square root of 144 is ", math.sqrt(144))
print(math.ceil(7.4))
print(math.floor(7.4))
print(math.log(8,2))
print(math.pow(4,3))
print(math.sin(60))
print(math.cos(60))
print(math.tan(45))

# Quadratic Formula
a = 2
b = 1
c = -1

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print("x1=", x1, "x2=", x2)

# Surface area and volume of a right circular cylinder
r = 1
h = 2

surface_area = 2*math.pi*r*h + 2*math.pi*r*r
volume = math.pi*r*r*h
print("The surface area is ", round(surface_area, 2))
print("The volume is ", round(volume, 2))






