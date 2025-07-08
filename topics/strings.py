

# Comparing string values

print("c > d:", "c" > "d")
print("c >= d:", "c" >= "d")
print("ab < ac:", "ab" < "ac")
print("ab <= ac:", "ab" <= "ac")
print("aa == aa:", "aa" == "aa")
print("a != b:", "a" != "b")
print("a in bca:", "a" in "bca")
print("a not in bc:", "a" not in "bc")
print('aples in apples:', "aples" in "apples")

# lower and upper methods

x = "fruits"
print(x.lower())
print(x.upper())
print("a.upper() == A:", "a".upper() == "A")

s_input =  "Today is a great DAY!"
print(s_input.lower())
print(s_input.upper())
print(len(s_input))

_s_input = "Z"
print(True if "a" <= _s_input.lower() <= "t" else False)

# String indexing

name = "Peterson"
print(name[0])
print(name[-1])

word = "chance"
print(word[-1] == word[5])

# String slicing
print(word[:5])
print(word[0:2])
print(word[2:6])

time_str = "13:46"
print(f"minutes: {time_str[3:5]}")
print(f"hours: {time_str[:2]}")

location = "classroom"
print(location[-3:-1])

greeting = "hi Leila"
name = greeting[3:]
print(name)

# String immutability

"""
Strings are immutable objects (once created, cannot be modified)
"""
_name = "Gianna"
# _name[0] = "*" # not accepted
print(_name)

greeting_msg = "Hello my fellow classmates"
print(greeting_msg[:6])
print("Hi" + greeting_msg[5:])

string_variable = "great"
indices = [0, 1]

for i in indices:
    string_variable = string_variable[:i] + '*' + string_variable[i+1:]

print(string_variable)
out = ""
for i in string_variable:
    if i != '*':
        out += i

print(out)

# Searching and testing strings

# in operator
print("ab in arbitrary: ", "ab" in "arbitrary")
print("a" in "an umbrella")

# for loop using in operator
for c in "string":
    print(c, end = "")
print()

count = 0
for c in "abca":
    if c == "a":
     count += 1
print(count)

# count method - counts the number of occurrences of a substring in a given string
print("weather".count("b"))
print("aaa".count("aa"))


# find method - returns the index of the first occurrence of a substring in a given string
print("banana".find("a"))
print("banana".find("c"))
print("b".find("banana"))

# index
"""
    performs similarly to the find() method in which the method returns the index of the
    first occurrence of a substring in a given string. The index() method assumes that the substring exists in the
    given string; otherwise, throws a ValueError
"""

time_string = "The time is 12:50"
index = time_string.index(":") # 14
print(index)
print(time_string[index+1:index+3]) # time_string[15:17] 50

print("school".index("o"))
# print("school".index("ooo")) # returns ValueError

sentence = "This is a sentence"
index = sentence.index(" ")
print(index)
print(sentence[:index])

input_str = "" # input("Enter a string: ")
print(input_str.count(" "))

out_str = ""
for i in input_str:
    if i != " ":
        out_str += i

print(out_str)

# String formatting

# replacement fields
print("Hey {}!".format("Bengio"))

s = "Dear {}, I'd like to take a {} course with Prof. {}."

print(s)
print(s.format("John", "programming", "Potter"))
print(s.format("Kishwar", "math", "Robinson"))

print("Hello {}!".format("Dallington"))

# named replacement fields
st = "Weather in {season} is {temperature}"
print(st.format(temperature="hot", season="summer"))

# Multiple use of a named argument
s = "Weather in {season} is {temperature}; very very {temperature}."

print(s)
print(s.format(season = "summer", temperature = "hot"))
print(s.format(temperature = "cold", season = "winter"))

# Numbered replacement fields
print("{1} {0}".format("Home", "Welcome"))
print("{0} {0} {1}".format("very", "cold"))

# string length and alignment formatting
"""
 {name:15} specifies that the minimum length of the string values that are passed to the name field is 15.
"""
print("{firstname:15} {lastname}".format(firstname = "Dallington", lastname = "Asingwire"))
print("{firstname:^15} {lastname}".format(firstname = "Dallington", lastname = "Asingwire"))
print("{firstname:<15} {lastname}".format(firstname = "Dallington", lastname = "Asingwire"))
print("{firstname:>15} {lastname}".format(firstname = "Dallington", lastname = "Asingwire"))

# formatting numbers
print("{:.7f}".format(0.9795))
print("{:.3f}".format(12))
print("{:+.2f}".format(12))
print("{:0>5d}".format(5))
print("{:.3s}".format("12.50"))

print('{0:.3f}'.format(3.141592))
print('{:1>3d}'.format(3))
print('{:+d}'.format(123))

numbers = [12.5, 2]
for i in numbers:
    print("{:0>6.2f}".format(i))


# splitting and joining strings

# split() splits a string into substrings
print("1-2-3-4-5".split("-"))
print("1 2 3 4 5 6".split())
print("1*2*3*".split('*'))
print("a year includes 12 months".split())
print("""This is a test""".split())

# join - concatenates a list of string values to form one output string
print((" ").join(['This', 'is', 'a', 'test']))
print(",".join(['A', 'beautiful', 'day', 'for', 'learning']))
print("sss".join(["1","2"]))
print("".join(["1", "2"]))

# seq = input("Enter a comma separated sequence of words: ")
# for word in seq.split(","):
#     print(word)

# Keep reading/storing input until a blank line.
food = []
while True:
    line = input("Order item: ")
    if line == "":
        break
    food.append(line)

# Repeat back the order, separated by commas.
if len(food) == 0:
    print("You ordered nothing")
elif len(food) == 1:
    print("You ordered", food[0])
elif len(food) == 2:
    print("You ordered", food[0], "and", food[1])
else:
    food[-1] = "and " + food[-1]
    print("You ordered", ", ".join(food))