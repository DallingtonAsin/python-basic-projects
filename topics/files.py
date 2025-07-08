import csv

from numba.cuda import const

directory = "./datasets"
file_obj = open(f"{directory}/file.txt")

# using read
str1 = file_obj.read()
print(str1)

# using readline
str2 = file_obj.readline()
print(str2)

# using readlines
print(file_obj.readlines())

file_obj.close()

num_obj = open(f"{directory}/num.txt")

firstline_split = num_obj.readline().split(":")
n = int(firstline_split[1])
print(n)

total = 0
nums = num_obj.readlines()
for i in range(n):
   total += int(nums[i])

avg = total / n
print(avg)

wr_obj = open(f"{directory}/output.txt", "w")
wr_obj.write("I am a nice guy from Uganda.\nI am a good software engineer.\nI support LFC!")
wr_obj.write("\nI like Python programming language")
wr_obj.close()


ap_obj = open(f"{directory}/num.txt", "a")
ap_obj.write("I read from this file numbers and printed their average.")
ap_obj.close()

fil_obj = open(f"{directory}/out.txt", "w")
fil_obj.write("Creating new content in a new file.")
fil_obj.close()

out_obj  = open(f"{directory}/out.log", "a")
out_obj.write("He is a good software engineer\nHe is a great innovator!")
out_obj.close()

filename = f"{directory}/currency.csv"

try:
    csv_obj = open(filename)
    rows = csv_obj.readlines()

    list_csv = []

    for row in rows:
        row = row.strip("\n")
        cells = row.split(",")
        list_csv.append(cells)

    print(list_csv)
except FileNotFoundError:
    print("File not found:", filename)


std_obj = open(f"{directory}/student.csv")
student_data =  std_obj.readlines()

csv_data = []
total_scores = 0
total_students = 0

for row in student_data[1:]:
    row = row.strip("\n")
    cell = row.split(",")
    score = float(cell[1])
    total_scores += score
    total_students += 1

avg_score = total_scores / total_students
print(avg_score)


def create_csv_file(file_name, fieldnames, data_list):
    try:
        with open(file_name, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for dict_row in data_list:
               writer.writerow(dict_row)
    except FileNotFoundError:
        print("File not found:", file_name)

# using built-in library csv to write data

# without using reusable function

with open(f'{directory}/student.csv', 'w') as file:
    fieldnames = ['student_id', 'score']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'student_id':123, 'score': 95 })
    writer.writerow({'student_id':213, 'score': 92 })
    writer.writerow({'student_id':111, 'score': 86 })
    writer.writerow({'student_id':555, 'score': 97 })
    writer.writerow({'student_id':621, 'score': 99 })
    writer.writerow({'student_id':777, 'score': 10 })
    writer.writerow({'student_id':312, 'score': 84 })
    writer.writerow({'student_id':391, 'score': 88 })
    writer.writerow({'student_id':398, 'score': 87 })
    writer.writerow({'student_id':444, 'score': 95 })


def get_type(word):
    try:
        int(word)
        return "int"
    except ValueError:
        try:
            float(word)
            return "float"
        except ValueError:
            return "str"


if __name__ == "__main__":
    for line in open(f"{directory}/data.txt"):
        for word in line.split():
            print(get_type(word), word, sep=": ")

# using a reusable function to create a csv file
data_obj = open(f"{directory}/population.txt")
pop_rows = data_obj.readlines()
data_list = []

for row in pop_rows[1:]:
    row = row.strip("\n")
    cell = row.split(",")
    dict_obj = {"Country": cell[0],"Population (2025)": cell[1],"Land Area (km²)": cell[2],"Density (people/km²)": cell[3]}
    data_list.append(dict_obj)

row_headers = ["Country", "Population (2025)", "Land Area (km²)", "Density (people/km²)"]
create_csv_file(f'{directory}/countries_data.csv', row_headers, data_list)

# Raising an exception

class Pizza:

    SIZES = {
        "S": ("Small", 5.99),
        "M": ("Medium", 7.99),
        "L": ("Large", 9.99),
        "XL": ("X-Large", 11.99),
    }

    def __init__(self, size):
        if size not in Pizza.SIZES:
            raise ValueError("Unknown piza size")
        self.size = size

    def __str__(self):
        name, price = Pizza.SIZES[self.size]
        return f"{name} pizza for ${price}"

pz_1 = Pizza("S")
pz_2 = Pizza("M")
pz_3 = Pizza("L")
print(pz_1, pz_2, pz_3, sep="\n")


word = input("Enter a word: ")

while True:
    f_name = input("Enter file name: ")
    file = f"{directory}/{f_name}"
    try:
     f_country = open(file)
     break
    except FileNotFoundError:
        print("File not found:", file)


country_info = f_country.readlines()

for row in country_info[1:]:
    row = row.strip("\n")
    cell = row.split(",")
    if word in cell[0]:
        print(cell[0], cell[1], cell[2], cell[3], sep=",")


def lookup(dictionary, search_term):
    hits = []
    for key in dictionary.keys():
        if search_term.lower() in key.lower():
            hits.append(key)
    if len(hits) == 0:
        raise KeyError("Key not found")
    elif len(hits) > 1:
        raise KeyError("Multiple keys found")
    else:
        key = hits[0]
        return key, dictionary[key]


if __name__ == "__main__":

    # Read books from the file
    books = {}
    for line in open(f"{directory}/books.csv"):
        title, isbn = line.split(",")
        books[title] = int(isbn)

    print("Books ===> ", books)
    # Try looking up some books
    for term in ["PREJ", "hob", "1984", "The"]:
        try:
            result = lookup(books, term)
            print("Found:", result)
        except KeyError as err:
            print("Error:", err)
        except ValueError as err:
            print("Error:", err)