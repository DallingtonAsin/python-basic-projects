
def menu():
    print(f'\n{"."*7}Menu{"."*7}\n1.Enter the word\n2.Exit\n')


def palindrome(word):
    word = word.lower()
    if len(word) == 1:
        print(f"This is a palindrome")
    else:
        if word[0] == word[-1]:
            palindrome(word[1:-1])
        else:
            print("This is not a palindrome")


while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            palindrome(input("Enter a word: "))
        elif choice == 2:
            break
        else:
            print("Invalid choice")
            continue
    except ValueError:
        print("Invalid choice entry!")
        continue