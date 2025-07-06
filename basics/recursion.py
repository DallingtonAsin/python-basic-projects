"""
 Recursion
"""

# Factorial of a number

def factorial(n):
    if n < 0:
        return -1
    else:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


print(f"Factorial of 5 is {factorial(5)}")

# generating fibonacci series

def fibonacci(n):
    if n < 0:
        return "Please enter a positive integer"
    else:
        if n == 0:
            return [0]
        elif n == 1:
            return [1]
        else:
            fibo_series = [0, 1]
            for i in range(2, n + 1):
                 fibo_series.append(fibo_series[i - 1] + fibo_series[i - 2])
            return fibo_series


print(fibonacci(10))

# summation of numbers from 0 to n

def rec_sum(n):
    if n < 0:
        return "Please enter a positive integer"
    else:
        if n == 0:
            return 0
        else:
            return n + rec_sum(n - 1)

val = 18
print(f"The summation of numbers from 0 to {val} is {rec_sum(val)}")

def digit_sum(n):
    if n < 0:
        print("The summation is not defined for negative integers.")
        return -1
    elif n < 10:
        return n
    else:
        return n%10 + digit_sum(n//10)

print(digit_sum(6721))


# Recursion with strings

def palindrome(word):
    word = word.lower()

    if len(word) <= 1:
        print("This is a palindrome")
    else:
        if word[0] == word[-1]:
            palindrome(word[1:-1])
        else:
            print("Not a palindrome")


palindrome("madam")

# Recursion with lists
def permu_check(list_1, list_2):
    if (list_1 is None and list_2 is None) or (len(list_1) == 0 and len(list_2) == 0):
        return True
    else:
        if list_2.count(list_1[0]) > 0:
            return permu_check(list_1.remove(list_1[0]), list_2.remove(list_1[0]))
        else:
            return False


num_list_1 = [1, 3, 9, 7, 3]
num_list_2 = [9, 1, 3, 3, 7]
print(permu_check(num_list_1.copy(), num_list_2.copy()))

# Write a recursive rem_dup() function that removes duplicates from a list.
# Ex: List [5, 5, 2, 1, 3, 1, 6] should result in an output list [5, 2, 1, 3, 6]

""" Find GCD using recursive implementation of Euclid's method """

def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(a, b-a)
    else:
        return gcd(a-b, a)


print("The gcd of 24 and 30 is", gcd(24, 30))


def power(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / ( x * power(x, abs(y)-1))
    else:
        return x * power(x, y-1)

print(power(2,4))
print(power(2, -4))


# Using recursion to solve problems

"""
   - using recursion to efficiently search a list
   - demonstrate a solution to solve the three tower problem
"""

""" Binary Search """
def binary_search(search_list, low, high, key):

    # Check base case
    if high > low:
        mid = (high + low) // 2

        # If element is present at the middle itself (base case)
        if search_list[mid] == key:
            return mid

        # Recursive case: check which subarray must be checked

        # Right subarray
        elif key > search_list[mid]:
            return binary_search(search_list, mid + 1, high, key)

        # Left subarray
        else:
            return binary_search(search_list, low, mid - 1, key)
    else:
        # Key not found (other base case)
        return "Not found"

in_list = [1, 3, 13, 16, 19, 22, 27, 32, 48, 66, 78, 99, 111, 122]

print(binary_search(in_list, 0, len(in_list)-1, 48))
print(binary_search(in_list, 0, len(in_list)-1, 86))


""" Solving the towers problem recursively """
def three_towers(N, source_tower, dest_tower, temp_tower):
    # Base case: simply move the single(bottom) ring from source to destination tower
    if N==1:
        print("Move ring 1 from tower", source_tower, "to tower", dest_tower)
        return # Exit when the base case is reached

    # Recursive case
    # Call the smaller version of the problem:
    # to move the N-1 stack to the middle tower

    three_towers(N-1, source_tower, temp_tower, dest_tower)

    # Move the N ring to the destination tower
    print("Move ring", N, "from tower", source_tower, "to tower", dest_tower)

    # Call the smaller version of the problem:
    # to now move the N-1 stack from the middle tower
    # to the destination

    three_towers(N-1, temp_tower, dest_tower, source_tower)


# Test code
print("Solution for 3 rings:")
three_towers(3, 't1', 't3', 't2') # t1, t2, t3 are the towers