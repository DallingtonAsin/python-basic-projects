
# Background, Input/Output, Variables, String Basics, Number Basics, Error Messages
# Comments, Why python

_name = "Annet"
print("My name is Dallington")
print(f"My mother is {_name}")

# print and input

# Output
print("Today", "is",  "a", "good day") # use of , (coma)
print("Today", "is",  "a", "good day", sep=" + ") # use of sep
print("My favourite color is red", end=" ")
print("I love Liverpool FC")

# Input
address  = input("Where do you come from?: ")
print(f"I come from {address}")

print("What is your favourite song?")
song = input()
print("My favourite song is:", song)

# Variables
team1 = "Liverpool"
team2 = "Chelsea"
print(team1, "versus", team2)
score1 = 4
score2 = 3
print("Final score: ", score1, "to", score2)

# String basics
check_str = "I hope you're not sad!"
str_2 = 'Peter said it is "Correct"'
print("The length of the string is:", len(str_2))

number = "12"
number_of_digits = len(number)  # Get length of the string
print("Number", number, "has", number_of_digits, "digits.")


fav_player = "Florian Wirtz"
print("My favorite player is "+ fav_player +" ")  # concatenation

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
fn_digits = len(first_name)
ln_digits = len(last_name)

print("Your first name is "+ str(fn_digits) +" letters long")
print("Your last name is "+ str(ln_digits) +" letters long")

name = "Freda"
feel = "happy"
print("Hi "+ name +"!")
print("I'm glad you feel " + feel +".")

# Number basics
x = 2.0
print(x, type(x))

# Arithmetic operators  (+,-,/,*)
p = 5
q = 3
print(p, "+", q, "=", p + q)
print(p, "-", q, "=", p - q)
print(p, "*", q, "=", p * q)
print(p, "/", q, "=", p / q)
print(p, "**", q, "=", p ** q)\

int_a = 10
float_a = 10.0
string_a = "10"
print(int_a, type(int_a))
print(float_a, type(float_a))
print(string_a, type(string_a))

meters = 10
meter2feet = 3.28
feet = meters  * meter2feet
print("10 meters in feet is", feet, "feet")

# Errors
# SyntaxErrors, NameErrors, and IndentationError


# Comments

# Display the menu options
print("Lunch Menu")
print("----------")
print("Burrito")
print("Enchilada")
print("Taco")
print("Salad")
print() # End of menu

# Get the user's preferences
item1 = input("Item #1: ")
item2 = input("Item #2: ")

"""
This is a docstring which is more like a multi-comem
"""


