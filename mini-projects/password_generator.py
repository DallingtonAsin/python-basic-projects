import string
import random


def display_menu():
    print(f'\n{"."*7}Password Choice Type{"."*7}\n1.Letters\n2.Digits\n3.Special characters\n4.Letters and special characters\n5.Letters and digits\n6.Letters, special characters, and digits\n7.Exit\n')

def generate_password(choice):

    options = {
        1: string.ascii_letters,
        2: string.punctuation,
        3: string.digits,
        4: string.ascii_letters + string.punctuation,
        5: string.ascii_letters + string.digits,
        6: string.ascii_letters + string.digits + string.punctuation
    }
    return options[choice]



while True:

    display_menu()

    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice in [1, 2, 3, 4, 5, 6]:
            try:
                length = int(input("Enter length of password: "))

                character_list = generate_password(user_choice)
                password_list = []

                for i in range(length):
                    random_char = random.choice(character_list)
                    password_list.append(random_char)

                password = "".join(password_list)
                print(f"Generated password: {password}")
            except ValueError as ve:
                print("Error:", ve)
        elif user_choice == 7:
            break
        else:
            print("Invalid choice")
            continue

    except KeyError as e:
            print("Error:", e)