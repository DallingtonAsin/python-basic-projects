"""
  A Python dictionary is a data type for storing the data in a key-value pair format
"""

# dictionary creation

"""
 - using {}
 - using dict()
"""

my_dict = {"Sunday": 1, "Monday": 2, "Tuesday": 3}
print(my_dict)
print(my_dict["Sunday"])
print(my_dict.keys())
print(my_dict.values())
print(type(my_dict))

fruit_prices = {"mango": 3500, "banana": 3000, "orange": 1500, "jackfruit": 2000}
print(fruit_prices)

# Creating a dictionary from a list of tuples
car_prices = [("fielder", 3.8), ("wish", 3.6), ("harrier", 3.4)]
car_prices_dict = dict(car_prices)
print(car_prices_dict)

# Creating a dictionary using keyword arguments.
student_marks = dict(mark=35, moses=45, peter=56, dallington=98)
print(student_marks)

# Creating a dictionary from another dictionary.
old_dict = {"apple": 2, "banana": 3, "orange": 4}
new_dict = dict(old_dict)

my_info = {"firstname": "Dallington", "lastname": "Asingwire",  "age": 28}
print(my_info)

# accessing the values using keys
print(my_info["firstname"])
print(my_info["lastname"])
print(my_info.get("Lastname", "does not exist"))

# modifying the dictionary

# inserting new items
my_info["weight"] = 56
my_info.update({"address": "Ntinda", "married": True})

# updating information
my_info["lastname"] = "Ninsiima"
my_info.update({"firstname": "Gianna"})

# deleting info
del my_info["age"]
deleted_prop = my_info.pop("weight")
print(deleted_prop)

print("Updated dictionary", my_info)
print()

"""
Dictionary keys, values, and both keys and values can be obtained 
using keys(), values(), and items()
"""
print("items => ", my_info.items())
print("List of items => ", list(my_info.items()))

print(f"Keys are {my_info.keys()}")
print(f"List of keys are {list(my_info.keys())}")
print(f"Values are {my_info.values()}")
print(f"List of values are {list(my_info.values())}")

print()

cars_dict = dict()
cars_dict["Mustang"] = 10
cars_dict["Volt"] = 3
print(cars_dict)

cars_dict.update({"Mustang": 2})
print(cars_dict)

cars_dict.pop("Volt")
print(cars_dict)

string_value = "This is a string"
characters = {}

for c in string_value:
    characters[c] = 1

print(characters)
print(len(list(characters.keys())))

"""
Conditional statements can be used with dictionaries to check if certain keys, values, or dictionary items exist
in the dictionary or if a value satisfies a particular condition.

"""

movies = {"The godfather": 1974, "Interstellar": 2014}

print(("Interstellar", 2014) in movies.items())
print(movies["The godfather"] < 2000)
print("Interstellar" in movies.keys())
print(1974 in movies.values())


# Looping through a dictionary

for key in my_info:
    print(key, ":", my_info[key])

print()
for key, value in my_info.items():
    print(f"{key}: {value}")

print()
for key in my_info.keys():
    print(f"{key}")

print()
for value in my_info.values():
    print(value)

string_value = "This is a string"
char_dict = {}

for i in string_value:
    if i in char_dict.keys():
     char_dict[i] += 1
    else:
     char_dict[i] = 1

print(char_dict)


fruit_count = {"banana": 2, "orange": 5, "peach": 5}
total_fruits = 0

for value in fruit_count.values():
    total_fruits += value

print(f"The total number of fruits is {total_fruits}")

company_org_chart = {
    "Marketing": {
       "ID234": "Jane Smith"
    },
        "Sales": {
        "ID123": "Bob Johnson",
        "ID122": "David Lee"
    },
        "Engineering": {
        "ID303": "Radhika Potlapally",
        "ID321": "Maryam Samimi"
    }
}

print(company_org_chart["Sales"]["ID122"])
print(company_org_chart["Engineering"]["ID321"])

# Dictionary comprehension
"""
   Dictionary comprehension is a concise and efficient way to create a dictionary in Python.
   {key_expression: value_expression for element in iterable}
"""

numbers = [1, 2, 3, 4, 5]

dict_ = { i: i*i for i in numbers if i % 2 == 0 }
print(dict_)

prices = {"apple": 1.99, "banana": 0.99, "orange": 2.49, "pear": 1.79}

# Create a dictionary of euro_prices
euro_prices = { product: round(price * 0.89, 2) for product, price in prices.items()}

# Print the content of the dictionary after the population
print(euro_prices)

employees = {
        1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
        1002: {"name": "Bob", "department": "Sales", "salary": 50000},
        1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
        1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
        1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

dept_employees = {}

for employee_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees.keys():
        dept_employees[dept] = {}
    dept_employees[dept][employee_id] = {"name": info["name"], "salary": info["salary"]}

print(dept_employees)

"""
Given a list, create a dictionary with two keys, "even" and "odd". The values associated with each key must
be the list of corresponding even and odd values in the given list.
:
input_list = [3, 5, 6, 1]
Prints {"even": [6], "odd":[3, 5, 1]}
"""

input_list = [3, 5, 6, 1]
input_dict = {"even": [], "odd": []}
for item in input_list:
    if item % 2 == 0:
        input_dict["even"].append(item)
    else:
        input_dict["odd"].append(item)

print(input_dict)