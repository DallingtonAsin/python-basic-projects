from sympy.physics.units import length

# Exercises

# Reverse an integer
int_val = 76542
val_str = str(int_val)
reversed_str = ""

for s in range(len(val_str) - 1, -1, -1):
    reversed_str += val_str[s]

reversed_int = int(reversed_str)
print(f"{int_val} when reversed yields {reversed_int}")




# Factorial

num_val = 6
factorial = 1

if num_val < 0:
    print("Factorial does not exist for negative numbers")
elif num_val == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(num_val, 1, -1):
        factorial *= i

print(f"The factorial of {num_val} is {factorial}")





# While loop

i = 1
while i< 10:
    print(i, sep=",", end=" ")
    i = i + 1

# A program printing all odd numbers between 1 and 10

print()
counter = 0
while counter <= 10:
    if counter % 2 == 1:
        print(counter, sep=",", end=" ")
    counter += 1


print()
animals = ["cow", "dog", "cat", "rabbit"]
for animal in animals:
    print(animal, sep= " ", end= " ")

print()

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

total = 0
number = n1
while number <= n2:
    if number % 2 == 1:
        total += number
    number += 1

print(f"Sum of odd numbers from {n1} to {n2} is {total}")


print()
while input() != "begin":
    pass


# for loop

name = "Atukunda"
for c in name:
    print(c, end = " ")
print()


# using range function in for loop

for e in range(5):
    print(e, end=" ")
print()

for k in range(0, 20):
    print(k, end=" ")
print()

for c in range(10, 50, 5):
    print(c, end = " ")
print()

input_str = input("What is your input string?: ")
count = 0

for c in input_str:
    if c == " ":
        count += 1

print(f"The total number of spaces in {input_str} is: {count}")


_n1 = int(input("Enter the first number: "))
_n2 = int(input("Enter the second number: "))

if _n1 < _n2:
    for num in range(_n1, _n2 + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()

    for n in range(_n2, _n1 - 1, -1):
        if n % 2 == 1:
            print(n, end=" ")
    print()
else:
    print("Error: The second number must be greater than the first number.")


# count the number of characters in a string

str_var = "A string"
count = 0

for c in str_var:
 count += 1
print(count)

# Nested loops

character = ''
for c in range(2):
    if c == 0:
        character = '*'
    else:
        character = '+'
    i = 4
    while i >= 1:
        print(i * character)
        i -= 1


print()

i = 1
while i <= 8:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    i += 1
    print()

hour = 7
minute = 0

while hour <= 9:
    while minute < 60:
        print(f"{hour:02d}:{minute:02d}")
        minute += 30
    hour += 1
    minute = 0

# Break statement

search_char = 'a'
user_string = "This is a string"
for i in range(len(user_string)):
    if user_string[i] == search_char:
        print(f"Found {search_char} at index {i}")
        break

print()

counter = 2
while True:
    if counter == 10:
        break
    print(counter, end=" ")
    counter += 1

print()

string_val = "Hello World"
for c in string_val:
    if c == " ":
     break
    print(c, end="")

print()

str_val = input("Enter a string value: ")
has_space_char = False

for c in str_val:
    if c == " ":
        has_space_char = True
        break

print("Found" if has_space_char else "Not Found")


# Continue

my_list = [1, 5, 7, 12, 5, 17, 9, 2, 4]
total = 0

for i in my_list:
    if i < 5:
        continue
    else:
        total += i

print(total)

# loop else

numbers_list = [11, 56, 78, 90, 7, 10, 89, 66, 3, 4]
search_num = 10

for b in numbers_list:
    if b == 10:
        print(f"Found {search_num}!")
        break
else:
    print(f"{search_num} is not in the list")

_total = 0
for v in numbers_list:
    if v >= 10:
        break
    _total += v
else:
    pass

print("The sum of numbers in the list less than 10 is", _total)