import math

# tuples

"""
Tuples are ordered and allow duplicates, like lists, but have different
mutability. An immutable object cannot be modified after creation. A mutable object can be modified after
creation. Tuples are immutable, whereas lists are mutable.
"""

my_tuple = (30, 45, 50, 30, 56)
print(my_tuple)
print(len(my_tuple))
print("First element in the tuple", my_tuple[0])
print("Last element in the tuple", my_tuple[-1])
print()

# creating a tuple from a list
list_of_grades = [90,88, 34, 67, 99]
grade_tuple = tuple(list_of_grades)
print(f"Tuple of grades {grade_tuple}\n")

str_1 = input("Input the first string: ")
str_2  = input("input the second string: ")
val_1 = int(input("Input the first number: "))
val_2  = int(input("input the second number: "))

val_tuple = (str_1, str_2, val_1, val_2)
print(f"Tuple of entered values {val_tuple}")




str = "Paul"
print("The first character from the left in Paul is", str[0]) # returns the first character in the string from the left
print("The first character from the right in Paul is", str[-1]) # returns first character from the right

# ord() function converts a character to a code point
print(ord(str[0]))

# chr() function converts a code point to a character
print(chr(80))

print(ord('A'))
print(ord('a'))

# Escape sequences
print("My name is Dallington\nI am a software engineer")
print("I am a Ugandan computer scientist\tI like innovating")
print("I heard he said he is \"good man\"")
print("\\He is a great guy!\\")

print("\"To me programming is more than an important practical art.\nIt is also a gigantic undertaking in the foundations of knowledge.\"\n\t\t\t-- Grace Hopper")

word = "CAT" # input("Input a word: ")
shift = 3 # int(input("Shift by how many letters? "))
new_word = ""

for letter in word:
    code_point = ord(letter) + shift
    new_letter = chr(code_point)
    new_word += new_letter

print("The word", word, "when shifted by", shift, "times yields",  new_word)

# Formatted Strings

# F-strings
animal = "dog"
sound = "barks"
print(f"The {animal} {sound}")

name = input("Enter a name: ")
noun = input("Enter a noun: ")
adj = input("Enter an adjective: ")
verb = input("Enter a verb ending in --ing: ")

print(f"{name}, the {adj} {noun}, likes to go {verb}.")


# Formatted numbers
print(f"{12345678:d}")
print(f"{12345678:,d}")
print(f"{12345678:.2f}")
print(f"{math.pi:f}") # default is 6 decimal places
print(f"{math.pi:.4f}") # round off to 4 dps
print(f"{math.pi:8.4f}") # rounded to 4 decimal places, at least 8 characters wide
print(f"{math.pi:08.4f}") # rounded to 4 decimal places, at least 8 characters wide, with leading zeros.


# Attempt 2
starting_hour =  int(input("Starting hour: "))
starting_minute =  int(input("Starting minute: "))
stopping_hour =  int(input("Stopping hour: "))
stopping_minute =  int(input("Stopping minute: "))
hourly_rate = float(input("Hourly rate: "))

start = starting_hour * 60 + starting_minute
stop = stopping_hour * 60 + stopping_minute
total_hours = ( stop - start ) / 60

total_payment = total_hours * hourly_rate

print(f"Worked {starting_hour}:{starting_minute:02d} to {stopping_hour}:{stopping_minute:02d}")
print(f"Total hours: {total_hours}")
print(f"Payment: ${total_payment}")


# Objects
# Every object has an identity, a type, and a value:

obj = 10.0
print(id(obj)) # returns id of an object
print(type(obj)) # returns type of an object
print(obj) # returns value of an object

# Lists basics
languages = ["C", "C++", "Java", "Python"]
print("The list of languages",languages)
print("The first language in the list is", languages[0])
print("The last language in the list is", languages[-1])
print("The length of the list is", len(languages))

# updating the list
languages[1] = "C#"

print("Updated list", languages)
print()

# List of numbers
numbers_list = [2, 23, 39, 6, -5]
numbers_list[2] = 35

print(numbers_list)
print(len(numbers_list))
