def count_digits_and_letters(input_string):
    digit_count = 0
    letter_count = 0

    for char in input_string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
    return digit_count, letter_count

user_input = input("Enter a string:")

digits, letters = count_digits_and_letters(user_input)
print(f"The number of digits is: {digits}")
print(f"The number of letters is: {letters}")
