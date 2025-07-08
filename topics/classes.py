"""
1. Object-oriented programming basics
2. Classes and instances
3. Instance methods
4. Overloading operators
5. Using modules with classes

"""
from topics.modules.area.classes import Triangle
from topics.modules.area.classes import Rectangle as Rct

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

std = Student("Dallington", 25)
print(f"His name is {std.name} and is aged {std.age} years old.")
std.print_details()

# Using modules with classes

tri = Triangle(6, 5)
print("Area of the triangle is", tri.area())
print("Perimeter of the triangle is", tri.perimeter())

rect = Rct(8, 4)
print("Area of the rectangle is", rect.area())
print("Perimeter of the rectangle is", rect.perimeter())


class VendingMachine:
    def __init__(self, num):
        self.count = num
        self.max = num

    def refill(self):
        self.count = self.max
        print("Refilled")

    def sell(self, order):
        self.count = self.count - order
        print(f"Sold: {order}")

    def print_stock(self):
        print(f"Current stock: {self.count}")

stock = int(input("Enter stock amount: "))
vm =  VendingMachine(stock)
vm.print_stock()
order_1 = int(input("Enter order: "))
vm.refill()
vm.sell(order_1)
vm.print_stock()
vm.refill()
vm.print_stock()


class Book:
    imprint = "Fantasy Tomes"
    def __init__(self):
        self.title = ""
        self.author = ""
        self.year = 0
        self.pages = 0

    def print_info(self):
        print(self.title, 'by', self.author, 'published by', self.imprint,
              'in', self.year, 'with', self.pages, 'pages')

book1 = Book()
book1.title = input("Enter a title for book 1: ")
book1.author = input("Enter the author for book 1: ")
book1.year = int(input("Enter the year for book 1: "))
book1.pages = int(input("Enter the pages for book 1: "))

book2 = Book()
book2.title = input("Enter a title for book 2: ")
book2.author = input("Enter the author for book 2: ")
book2.year = int(input("Enter the year for book 2: "))
book2.pages = int(input("Enter the pages for book 2: "))

book1.print_info()
book2.print_info()

class FlightTicket:
    airline = "Oceanic Airlines"
    airline_code = "OA"

    def __init__(self, flight_num = 1, airport = "JFK", gate = "T1-1", time = "8:00", seat = "1A", passenger = "Uknown"):
        self.flight_num = flight_num
        self.airport = airport
        self.gate = gate
        self.time = time
        self.seat = seat
        self.passenger = passenger

    def print_info(self):
            print('Passenger', self.passenger, 'departs on flight #', self.flight_num, 'at', self.time, 'from', self.airport, self.gate, 'in seat', self.seat)

flight_num = int(input("Enter flight number: "))
airport = input("Enter airport: ")
gate = input("Enter gate: ")
time = input("Enter time: ")
seat = input("Enter seat: ")
passenger = input("Enter passenger: ")

ticket = FlightTicket(flight_num, airport, gate, time, seat, passenger)
ticket.print_info()


"""
    Magic methods are special methods that perform actions for users, typically out of view of users. Magic
    methods are also called dunder methods, since the methods must start and end with double underscores (__).
    Ex: __init__() is a magic method used alongside __new__() to create a new instance and initialize
    attributes with a simple line like eng = Engineer(). A programmer can explicitly define a magic method in a
    user-defined class to customize the method's behavior.
"""

class Engineer:

    dep_id = "ENG"

    def __init__(self, e_id = 0, name = "", role = ""):
        self.e_id = e_id
        self.name = name
        self.role = role

    # magic method
    def __str__(self):
        return (
            f'ID: {self.e_id}\nName: {self.name}\nRole: {self.role}'
        )


print()
eng_1 = Engineer(5270, "Ali Song", "Full-Stack Engineer")
print(eng_1.__str__())


# Overloading operators
"""
    Operator overloading refers to customizing the function of a built-in operator. Arithmetic operators are
    commonly overloaded to allow for easy changes to instances of user-defined classes
"""

class Account:
    def __init__(self, name = "", amount = 0):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}: ${self.amount}"

    def __add__(self, other):
        return Account(self.name + ', '+ other.name, self.amount + other.amount)

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __eq__(self, other):
        return self.amount == other.amount

acct_a = Account("John", 100)
acct_b = Account("Fred", 300)
print(acct_a + acct_b)
print(acct_a > acct_b)
print(acct_a == acct_b)
print(acct_a < acct_b)


class ExerciseLog:

    def __init__(self, e_type, duration):
        self.e_type = e_type
        self.duration = duration

    def __str__(self):
        return f"{self.e_type}: {self.duration} minutes"

    def __add__(self, other):
        if self.e_type != other.e_type:
            return ExerciseLog( f"{self.e_type} and {other.e_type}", self.duration + other.duration)
        else:
            return ExerciseLog(self.e_type,  self.duration + other.duration)


type1 = input("Exercise Type 1: ")
duration1 = int(input("Duration for exercise Type 1: "))
exe_log_1 = ExerciseLog(type1, duration1)

type2 = input("Exercise Type 2: ")
duration2 = int(input("Duration for exercise Type 2: "))
exe_log_2 = ExerciseLog(type2, duration2)

print(exe_log_1 + exe_log_2)


