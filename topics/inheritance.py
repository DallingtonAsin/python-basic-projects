
class Employee():
    count = 0 # class attribute

    def __init__(self):
        Employee.count += 1
        self.e_id = Employee.count
        self.hire_year = 2025

    def emp_display(self):
        print(f"Employee {self.e_id} hired in {self.hire_year}")

    def print_company(self):
        print("Employee works at Stark Industries")

    def print_info(self):
        print("Employee", self.e_id, "was hired in", self.hire_year)

# Define Developer class
class Developer(Employee):

    def __init__(self, lang_xp=None):
        super().__init__()
        if lang_xp is None:
            lang_xp = ["Python", "C#", "Java"]
        self.lang_xp = lang_xp

    def print_info(self):
        super().print_info()
        print(f"Language(s): {self.lang_xp}")

    def update_codebase(self):
        print("Employee has updated the codebase")

    def dev_display(self):
        print(f"Proficient in {self.lang_xp}")

python_dev = Developer()

# Call Employee and Developer methods
python_dev.update_codebase()
python_dev.print_company()
python_dev.emp_display()
python_dev.dev_display()
python_dev.print_info()

class Polygon:
    def p_disp(self):
        print("Object is a Polygon")

class Rectangle(Polygon):
    def r_disp(self):
        print("Object is a Rectangle")

class Square(Rectangle):
    def s_disp(self):
        print("Object is a Square")


polygon = Polygon()
polygon.p_disp()

rectangle = Rectangle()
rectangle.p_disp()
rectangle.r_disp()

square = Square()
square.p_disp()
square.r_disp()
square.s_disp()

class Dessert:
    def __init__(self):
        self.ingredients = ["butter", "sugar", "eggs", "flour"]

# Define Child class
class Cupcake(Dessert):
    def __init__(self):
        super().__init__()
        self.ingredients = ["butter", "sugar", "eggs", "flour"]
        self.frosting = "buttercream"

    def display(self):
        print(f"Made with {self.ingredients} and topped with {self.frosting} frosting")

bday_cake = Cupcake()
bday_cake.display()

# Overriding Methods

class Plant:
    def display(self):
        print("I am a plant")

class Mint(Plant):
    def display(self):
        print("I am a mint")

class Lavender(Mint):
    def display(self):
     print("I'm a lavender")

mint = Mint()
mint.display()

plant = Plant()
plant.display()

lavender_1 = Lavender()
lavender_1.display()


class WeeklyEvent:
    def __init__(self, name, day):
        self.name = name
        self.day = day

class OnlineWeeklyEvent(WeeklyEvent):
    def __init__(self, name, day, link):
        super().__init__(name, day)
        self.link = link

    def invite(self):
        print(f"Join \"{self.name}\" on {self.day}s")
        print(f"Link: {self.link}")


link_1 = "stream.link/647711"
c_event = OnlineWeeklyEvent("Code with Dallington", "Saturday", link_1)
c_event.invite()


# Polymorphism

class Tax:
    def __init__(self, value):
        self.value = value

    def calc_tax(self):
        print("Calculating tax")
        total = 0.10 * self.value  # To replace with calculation
        return total


class ContractTax:
    def __init__(self, value):
        self.value = value

    def calc_tax(self):
        print("Calculating contracts tax")
        total = 0.15 * self.value  # To replace with calculation
        return total


my_tax = ContractTax(value=1000)  # Replace 1000 with any value
result = my_tax.calc_tax()
print(f"Total tax: ${result}")


class Pet():
    def display(self):
        print("Clinic patient: Pet")

# Define Bird class
class Bird(Pet):
    def display(self):
        print("Pet type: Bird")

# Define Finch class
class Finch(Bird):
    def display(self):
        print("Pet type: Finch")

bird_1 = Bird()
bird_1.display()
finch_1 = Finch()
finch_1.display()

# Hierarchical inheritance - multiple classes inherit from a single class

class ChoirMember:
    def display(self):
     print("Current choir member")


class Soprano(ChoirMember):
    def display(self):
        super().display()
        print("Part: Soprano")


class Soprano1(Soprano):
    def display(self):
        super().display()
        print("Division: Soprano 1")


class Alto(ChoirMember):
    def display(self):
        super().display()
        print("Part: Alto")


class Tenor(ChoirMember):
    def display(self):
        super().display()
        print("Part: Tenor")


class Bass(ChoirMember):
    def display(self):
        super().display()
        print("Part: Bass")


mem_10 = Alto()
mem_13 = Tenor()
mem_15 = Soprano1()

mem_10.display()

class Instrument:
    def __init__(self, name = "Unknown"):
        self.owner = name

class Woodwind(Instrument):
    def __init__(self, name = "Unknown", material = "Wood"):
        super().__init__(name)
        self.material = material

class String(Instrument):
    def __init__(self, name = "Unknown", num_strings = 4):
        super().__init__(name)
        self.num_strings = num_strings


flute_1 = Woodwind()
cello_1 = String()

print(f"This flute belongs to {flute_1.owner} and is made of {flute_1.material}")
print(f"This cello belongs to {cello_1.owner} and has {cello_1.num_strings} strings")

# Multilevel inheritance and mixin classes
"""
Multilevel inheritance - one class inherits from multiple classes
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal is eating")

class Mammal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Mammal makes sound")

class Person(Animal, Mammal):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self):
        print(f"{self.name} is both a mammal and animal")


person = Person("Dallington")
person.display_info()
person.make_sound()
person.eat()

"""
Mixin classes promote modularity and can remove the diamond problem. A mixin class:
    • Has no superclass
    • Has attributes and methods to be added to a subclass
    • Isn't instantiated (Ex: Given MyMixin class, my_inst = MyMixin() should never be used.)
"""

class Business:
    def process_order(self):
        print("Processing order")

class Restaurant(Business):
    def process_order(self):
        print("Processing meal order")

class OnlineShop(Business): # Change to mixin class
    def process_order(self):
        print("Processing online order")

class OnlineMixin():
    def process_online(self):
        print("Connecting to server")


class FoodFast(Restaurant, OnlineMixin):
    def process_order(self):
        # Call mixin method
        super().process_order()
        self.process_online()
        print("Enjoy your FoodFast order")

franchise_1 = FoodFast()
franchise_1.process_order()








