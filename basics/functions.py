def welcome():
    print("Welcome to functions class")


def calculate_area(length, width):
    return length * width

welcome()

area = calculate_area(5, 5)
print(f"Area: {area}")
print()

def concessions():
    print("Food/Drink Options:\nPopcorn: $8-10\nCandy: $3-5\nSoft drink: $5-7")

concessions()

def laundromat_info():
    print("Liam's Laundry\n7a - 11p")
    washers_open()
    dryers_open()

def washers_open():
    washer_count = int(input("Enter the washer count: "))
    print(f"Open washers: {washer_count}")

def dryers_open():
    dryer_count = int(input("Enter the dryer count: "))
    print(f"Open dryers: {dryer_count}")

laundromat_info()

def accepted():
    print("Thank you for accepting the terms.")

def rejected():
    print("You have rejected the terms. Thank you.")

def terms():
    response = input("Do you accept the terms and conditions?: ")
    if response == "Y":
        accepted()
    else:
        rejected()

no_of_users = int(input("How many users do you want to create?: "))
for i in range(no_of_users):
    terms()

def battle_royale():
    players_count = int(input("Enter the number of players: "))
    calculated_num = 3 - players_count
    find_teammates(calculated_num)
    print("Match starting . . .")

def find_teammates(num):
    print("Finding", num, "players...")

def practice():
  desired_map = input("Enter the desired map: ")
  print(f"Launching practice on {desired_map}")

game_mode = input("Enter game mode: ")
if game_mode == "br":
    battle_royale()
else:
    practice()

def convert_temps(temps, unit):
    if unit == "F":
        for i in range(len(temps)):
            temps[i] = (temps[i]-32) * 5/9
            unit = "C"
    else:
        for i in range(len(temps)):
            temps[i] = (temps[i]*9/5) + 32
            unit = "F"

# Weekend temperatures in Fahrenheit.
wknd_temps = [49.0, 51.0, 44.0]
deg_sign = u"\N{DEGREE SIGN}" # Unicode
metric = "F"

# Convert from Fahrenheit to Celsius.
convert_temps(wknd_temps, metric)
for temp in wknd_temps:
 print(f"{temp:.2f}{deg_sign}{metric}", end=" ")


def print_area(b, h):
    t_area = b * h * 0.5
    print(f"Triangle area: {t_area}")

base = float(input("Enter base: "))
height = float(input("Enter height: "))
print_area(base, height)


def print_scores(test_scores, bonus):
    for score in test_scores:
        print(f"{score} would be updated to {score + bonus}")

print_scores([67, 68, 72, 71, 69], 10)


def calc_sqft(length, width):
    sqft = length * width
    return
print(calc_sqft(5, 6))
print()


def calc_mpg(miles, gallons):
    if gallons > 0:
        mpg = miles/gallons
        return mpg
    else:
        print("Gallons can't be 0")
        return -1

car_1_mpg = calc_mpg(448, 16)
print("Car 1's mpg is", car_1_mpg)
car_2_mpg = calc_mpg(300, 0)
print("Car 2's mpg is", car_2_mpg)

def days_alive(age):
    return round(age * 365.24)
age = int(input("Enter your age: "))
print(F"You have been alive about {days_alive(age)} days")


def avg_list(values):
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

values_list = [12, 16, 19, 24, 56]
print(f"The average of values in {values_list} is {avg_list(values_list)}")


def donate(amount = 5, name = "Anonymous", msg = ""):
    print(f"{name} donated {amount} credits: {msg}")

donate()
donate(msg="great stream", name="Tim")
donate(10, "user123", "good luck")
print()