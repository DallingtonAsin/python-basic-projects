"""
1 Modifying and iterating lists
2 Sorting and reversing lists
3 Common list operations
4 Nested lists
5 List comprehensions

"""

students = ["Conrad", "James", "David", "Isaac", "Moses"]
print(students)

# Add new student
students.append("Dallington")
print(students)

# Remove a student
students.remove("James")
print(students)

# pop a list
students.pop()
print(students)

# iterating a list
for student in students:
    print(student, end= " ")

print()
for i in range(len(students)):
    print(students[i], end=" ")

print()

sports = ["baseball", "football", "tennis", "table tennis"]

sports.append("volleyball")
sports.remove("football")
sports.append("soccer")
print(sports)

for sport in sports:
    if sport == "soccer":
        print("Found!")
        break

num_list = [38, 92, 23, 16, 10, 5, 100]
print(num_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

dance_list = ["Stepping", "Ballet", "Salsa", "Kathak", "Hopak", "Flamenco","Dabke"]

dance_list.sort()
print(dance_list)

dance_list.reverse()
print(dance_list)

board_games = ["go", "chess", "scrabble", "checkers"]
board_games.sort()
print(board_games)

_num_list = [3, 32, -23, 699, 75, -101, 22, 45, 94, -3, 2]

_num_list.sort()
print(_num_list)

_num_list.reverse()
print(_num_list)

# List operations

# numbers
print(f"The maximum number in {num_list} is {max(num_list)}")
print(f"The minimum number in {num_list} is {min(num_list)}")
print(f"The sum of numbers in {num_list} is {sum(num_list)}")
print(sum([1.2, 2.1, 3.2, 5.9]))

# strings
print(f"The maximum number in {board_games} is {max(board_games)}")
print(f"The minimum number in {board_games} is {min(board_games)}")
print(min(["Lollapalooza", "Coachella", "Newport Jazz festival", "Hardly Strictly Bluegrass", "Austin City Limits"]))

# creating a copy of the list
my_list = ["Cat", "Dog", "Hamster"]
list2 = my_list.copy()
list2[2] = "Pigeon"
print(max(my_list))

word_list = ["exercise", "is", "truly", "a", "useful", "coding"]
wisdom = word_list.copy()
wisdom.sort()

word_sentence = ""
wisdom_sentence = ""

for word in word_list:
    word_sentence += word + " "

for wise_word in wisdom:
    wisdom_sentence += wise_word + " "

print(word_sentence)
print(wisdom_sentence)

# Nested lists
arr = [[12, 15, 70], [20, 45, 78], [90, 11, 34]]
for row in arr:
    for num in row:
        print(num, end=" ")
    print()

print()
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end=" ")
    print()

# multiplying 2 matrices


# List compressions
"""
A list comprehension is a Python statement to compactly create a new list using a pattern.
list_name = [expression for loop_variable in iterable]
"""

square_list = [i*i for i in range(1, 11)]
print(square_list)

words_list = ["one", "two", "red", "blue"]
poem_lines = [w + " fish" for w in words_list]

for line in poem_lines:
 print(line)

 a_list = [1, 2, 3, 4, 5]
 b_list = [ i+2 for i in a_list]
 print(b_list)

 """
  Filtering using list comprehensions
  list_name = [expression for loop_variable in container if condition]
 """

 even_num_list = [ i+2 for i in a_list if i % 2 == 0]
 print(even_num_list)

 my_list = [21, -1, 50, -9, 300, -50, 2]
 new_list = [m for m in my_list if m < 0]
 print(new_list)

 my_string = "This is a home."
 vowel_list = [i for i in my_string if i in 'aeiou']
 print(vowel_list)

 new_list = [r for r in range(0, 21, 2) if r % 2 != 0]
 print(new_list)


 word_list = ["notebook", "capsule", "ruler", "divider", "compass", "chart"]
 five_word_list = [word for word in word_list if len(word) == 5]
 print(five_word_list)

 # A list of book titles
 book_list = ["Pachinko", "A Hitchhiker's Guide to the Galaxy", "Moby Dick", "Beloved", "A Farewell to Arms",  "Anna Karenina", "The Golden Notebook"]
 a_books = [book for book in book_list if book[0] == 'A' ]
 a_books.sort()
 print(a_books)
