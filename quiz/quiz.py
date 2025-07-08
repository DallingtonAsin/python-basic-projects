
# Print first 10 natural numbers using while loop

for i in range(1, 11):
    print(i, end=" ")

print("\n")

"""
    Write a Python code to print the following number pattern using a loop.
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5
"""

for i in range(1, 6):
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()

print()

# Calculate sum of all numbers from 1 to a given number
input_num = 10
total = 0
for x in range(1, input_num + 1):
    total += x

print(f"The sum of numbers from 1 to {input_num} is {total}")
print()

# Print multiplication table of a given number
val = 2
for i in range(1, 11):
    print(i*val, end= " ")
print()

"""
Write a Python program to display only those numbers from a list that satisfy the following conditions
    - The number must be divisible by five
    - If the number is greater than 150, then skip it and move to the following number
    - If the number is greater than 500, then stop the loop
"""
print()

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
        if num > 500:
            break
        elif num > 150:
            continue
        elif num % 5 == 0:
            print(num, end=" ")

print()

# Count the total number of digits in a number
n = 76541
counter = 0
while n != 0:
    n = n // 10
    counter = counter + 1

print(f"The total number of digits is {counter}")

"""
Write a Python program to print the reverse number pattern using a for loop.
    5 4 3 2 1 
    4 3 2 1 
    3 2 1 
    2 1 
    1
"""
print()

for i in range(5, 0, -1):
   for j in range(i, 0, -1):
       print(j, end= " ")
   print()

print()

# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i], end=" ")

print()

# Display numbers from -10 to -1 using for loop
for val in range(-10, 0, 1):
    print(val, end=" ")

print()

# Display a message “Done” after the successful execution of the for loop
for i in range(5):
    print(i)
else:
 print("Done")


s = 25
e = 50
for i in range(s, e+1):
    is_prime =  True
    divisible_list = [j for j in range(2, i) if i % j == 0]
    if len(divisible_list) > 0 or i < 0:
        is_prime = False
    if is_prime:
        print(i, end=" ")
print()

# Display Fibonacci series up to 10 terms
def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        series = [0, 1]
        for i in range(2, n+1):
            series.append(series[i - 1] + series[i - 2])
        return series

print("First 10 fibonacci series:", fibonacci(10))

# Find the factorial of a given number
def factorial(n):
    if n < 0:
        return "Negative numbers don't have factorials."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 6 is", factorial(6))

# Reverse a integer number
number = 76542
reversed_number = 0
while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = number // 10

print(f"Reversed number of 76542 is {reversed_number}")


# Print elements from a given list present at odd index positions
#  E.g my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] should yield 20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i, num in enumerate(my_list):
    if i % 2 == 1:
        print(num, end= " ")

print()

# Calculate the cube of all numbers from 1 to a given number
n = 6
for num in range(1, n+1):
    print(f"Current Number is : {num}  and the cube is {num*num*num}")

n= 5
val = 2
total = 0

for i in range(1, n+1):
    num_str = str(val) * i
    num_int = int(num_str)
    total += num_int

print("Total=", total)

