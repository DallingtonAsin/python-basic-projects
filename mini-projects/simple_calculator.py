from modules.calculator import add, multiply, subtract, divide

def menu():
    print(f'OPERATION CHOICES\n{"."*20}\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\n')


print(f'{"."*35}\nWelcome to our simple calculator\n{"."*35}\n')

while True:

    # display menu
    menu()

    try:
        choice = int(input("Enter choice: "))
        if choice in [1, 2, 3, 4]:
            try:
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print()

                if choice == 1:
                    print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
                elif choice == 2:
                    print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
                elif choice == 3:
                    print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
                elif choice == 4:
                    print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
                else:
                    print("Unknown operation")
                    continue

            except ValueError:
                print("Error: Please enter a number.")
                continue
        elif choice == 5:
            exit(0)
        else:
            print("Invalid choice. Please try 1, 2, 3 or 4\n")
            continue
    except ValueError:
        print("Invalid choice. Please try 1, 2, 3 or 4\n")
        continue


