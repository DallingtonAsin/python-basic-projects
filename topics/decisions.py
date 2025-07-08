"""
1 Boolean values
2 If-else statements
3 Boolean operations
4 Operator precedence
5 Chained decisions
6 Nested decisions
7 Conditional expressions
"""

# Boolean values

is_dessert = True
print("is Egypt a desert?", is_dessert)

# bool() - converts a value to boolean

# zero number or empty string - False
print(bool(0))
print(bool(""))

# any non-zero number and non-empty string - True
print(bool(-1))
print(bool("Darius"))
# print(bool(input()))


# Converting booleans to numeric types and strings
is_on = True
print(float(is_on))
print(str(is_on))
print(int(is_on))

# Comparison operators ( ==, !=, <, >, <=, >=)
print("14 <= 13:", 14 <= 13)  # False
print("0 != 0.4:", 0 != 0.4) # True
print("4 < 4.0:", 4 < 4.0)  # False
# print('2 > "ab":', 2 > "ab") # Error
print('"cilantro" == "coriander"', "cilantro" == "coriander") # False
print('"dog" < "cat"', "dog" < "cat") # False

day_of_the_week = input("Enter day of the week: ")
is_love = day_of_the_week.lower() == "friday"
print("Is Love:", is_love)

number = int(input("Enter a number: "))
is_even = number % 2 == 0
print(number, "is even:", is_even)

# If else statements

age = 5
if age < 12:
    print("Discount for children is available")

is_raining = True
print("Have a great day.")
if is_raining:
    print("Don't forget about umbrella!")
print("See you soon!")

num = -10
if num < 0:
    num = 25
if num < 100:
    num = num + 50

print("num =", num)

positive_num = int(input("Enter a positive number:"))
if positive_num < 0:
 print("Negative input set to 0")
positive_num = 0
print("positive_num =", positive_num)

# If else statement

temp = float(input("Enter temperature: "))
unit = input("Enter the unit (f/c): ")
is_fahrenheit = unit.lower() == "f"

if is_fahrenheit:
    result = (temp - 32) * 5 / 9
else:
    result = (temp * 5/9) + 32

print(temp, unit, "is equal to ", result, "C" if is_fahrenheit else "F")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == 0:
    b = int(input())

c = a / b
print(f"The result is: {c}")


# Boolean operations

# Logical and
_age = int(input("How old are you?: "))
day = input("What is today?: ")

if _age >= 18 and day.lower() == "friday":
    print("You can join the party")
else:
    print("You can not join the party")


# Logical or
is_in_band = input("Are you in the band?(yes/no): ")
is_in_choir = input("Are you in the choir?(yes/no): ")

if is_in_band.lower() == 'yes' or is_in_choir.lower() == 'yes':
    print("You will perform at the concert")
else:
    print("You will not perform at the concert")


# Logical not
is_power_off = False
if not is_power_off:
    print("The computer is on")
else:
    print("Please power on the computer because it is off")


speed = int(input("The speed of your car is: "))
if 45 <= speed < 70:
    print("Good driving")
else:
    print("Follow the driving limits")


# Chained decisions
# if elif else


size = input("Enter the US Size: ")

if size == "B":
    diameter = 2.25
elif size == "C":
    diameter = 2.75
elif size == "D":
    diameter = 3.25
elif size == "E":
    diameter = 3.5
elif size == "F":
    diameter = 3.75
elif size == "G":
    diameter = 4.0
else:
    diameter = -1.0

print(f"{diameter} mm")

wavelength = int(input("Enter the wavelength in nanometers: "))

if 380 < wavelength < 449:
    color = "Violet"
elif 450 < wavelength < 484:
    color = "Blue"
elif 485 < wavelength < 499:
    color = "Cyan"
elif 500 < wavelength < 564:
    color = "Green"
elif 565 < wavelength < 589:
    color = "Yellow"
elif 590 < wavelength < 624:
    color = "Orange"
elif 625 < wavelength < 750:
    color = "Red"
else:
    color = ""

print("Color:", color)

# Nested decisions

game = int(input("What game do you play?: "))
players = int(input("How many players do you play?: "))

if game == 1:
    if players < 2:
        print("Not enough players")
    elif 2 <= players <= 4:
        print("Ready to start")
    elif players > 4:
        print("Too many players")
if game == 2:
    if players < 3:
        print("Not enough players")
    elif 3 <= players <= 6:
        print("Ready to start")
    elif players > 6:
        print("Too many players")


print("Lunch Meal Options\n1:Caesar salad\n2:Spicy chicken wrap\n3:Butternut squash soup\n")
print("Dinner Meal Options\n1:Baked salmon\n2:Turkey burger\n3:Mushroom risotto\n")
menu_choice_str = input("Enter menu choice (lunch/dinner): ")
user_menu_choice = int(input("Enter food choice: "))

if menu_choice_str.lower() == "lunch":
    if user_menu_choice == 1:
        order = "Caesar salad"
    elif user_menu_choice == 2:
        order = "Spicy chicken wrap"
    elif user_menu_choice == 3:
        order = "Butternut squash soup"
elif menu_choice_str.lower() == "dinner":
    if user_menu_choice == 1:
        order = "Baked salmon"
    elif user_menu_choice == 2:
        order = "Turkey burger"
    elif user_menu_choice == 3:
        order = "Mushroom risotto"

print(f"Your order: {order}")


# Conditional expressions

x = 5
response = 'even' if x % 2 == 0 else 'odd'
print(response)

ping = int(input("Enter ping value: "))
ping_report = "low to average" if ping < 150 else "too high"
print(ping_report)