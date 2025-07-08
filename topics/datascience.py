import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

directory = "./datasets"

numbers = [[-1, 2, 0], [5,7, 4], [8, 3, 1]]
arr1 = np.array(numbers)
print(arr1)

arr2 = np.zeros((2, 2))
print(arr2)

arr3 = np.ones((3, 3))
print(arr3)

print(arr1 + arr3)


# Pandas

# Dataframe from a dictionary

data = {
  "Name": ["Emma", "Gireeja", "Sophia"],
  "Age": [15, 28, 22],
  "City": ["Dubai", "London", "San Jose"]
}

dt = pd.DataFrame(data)
print(dt)
print()

# Dataframe from a list
data = [["Emma", 15, "Dubai"], ["Gireeja", 28, "London"], ["Sophia", 22, "San Jose"]]
columns = ["Name", "Age", "City"]
dt1 = pd.DataFrame(data, columns=columns)
print(dt1)
print()

# Dataframe from a Numpy array

data = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [2, 3, 4]
])
columns = ["A", "B", "C"]
dt2 = pd.DataFrame(data, columns=columns)
print(dt2)

# Dataframe from a csv

data = pd.read_csv(f"{directory}//student.csv")
print(data)
print(data.loc[0, "student_id"])
print(data.iloc[3, 1])


# Dataframe from excel
try:
    data = pd.read_csv(f"{directory}//student.xlsx")
    print(data)
except FileNotFoundError as err:
    print("File not Found", err)


days = {
    'Season': ['Summer', 'Summer', 'Fall', 'Winter', 'Fall', 'Winter'],
    'Month': ['July', 'June', 'September', 'January', 'October', 'February'],
    'Month-day': [1, 12, 3, 7, 20, 28],
    'Year': [2000, 1990, 2020, 1998, 2001, 2022]
}
df = pd.DataFrame(days)
print(df)
print()

print("The first 4 rows of the data frame")
print(df.head(4)) # head() returns the first 5 rows (default is 5)
print()

print("The last 3 rows of the data frame")
print(df.tail(3)) # tail() returns the last 5 rows (default is 5)
print()

print("Information about the dataframe\n")
print(df.info()) # provides a summary about the dataframe
print()

print(df.describe()) # Generates column counts, mean, standard deviation, maximum, minimum
print()

print(df.value_counts("Season")) # Counts the occurrences of unique values in a column when a column is passed as an argument and presents them in descending order.
print()

print(df["Season"].unique()) # Returns an array of unique values in a column when called on a column.

student_df = pd.read_csv(f"{directory}//student.csv")
print(student_df)
print(student_df.loc[0, "student_id"])
print(student_df.iloc[3, 1])

"""
 Data slicing - refers to selecting a subset of rows and/or columns from a DataFrame. Slicing can be
performed using ranges, lists, or Boolean conditions.

 Slicing using ranges: Ex: df.loc[start_row:end_row, start_column:end_column] selects rows and
columns within the specified ranges.
• Slicing using a list: Ex: df.loc[[label1, label2, ...], :] selects rows that are in the list [label1,
label2, ...] and includes all columns since all columns are selected by the colon operator.
• Slicing based on a condition: df[condition] selects only the rows that meet the given condition.

"""

# Slicing based on a condition
df_sel = student_df.loc[student_df["student_id"] == 111]
print(df_sel)

# Slicing using ranges
df_sl = student_df.loc[0:3, ["student_id"]]
print(df_sl)

print(student_df.iloc[1])

"""
 Data filtering involves selecting rows or columns based on certain conditions. Ex: In the expression
 df[df['column_name'] > threshold]
"""

data = {
    "Column 1": ["A", "B", "C", "D", "E"],
    "Column 2": [np.nan, 200, 500, 0, -10],
    "Column 3": [True, True, False, np.nan, np.nan]
}
df = pd.DataFrame(data)
print(df)
print("Sum of null values", df.isnull().sum())
print("\n")
print(df.isnull())

df["Column 2"] = df["Column 2"].fillna(df["Column 2"].mean())
print(df)

df = df.dropna()
print(df)

# Bar graph
courses = ["Course A", "Course B", "Course C"]
scores = [20, 45, 78]

plt.title("Courses vs Scores")
plt.xlabel("Courses")
plt.ylabel("Scores")
plt.bar(courses, scores)
plt.show()

# Line graph
month = ["Jan", "Feb", "Mar", "Apr", "May"]
inflation = [6.41, 6.04, 4.99, 4.93, 4.05]
plt.plot(month, inflation, label="Inflation", linestyle="-", marker="o", color="red")
plt.title("Monthly Inflation in 2025")
plt.xlabel("Month")
plt.ylabel("Inflation")
plt.show()

#  Scatter plot

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 8, 6, 4, 2, 5, 7, 9, 3, 1]
plt.scatter(x, y, marker="o", color="orange")
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Histogram plot

data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor="black")
plt.title("Histogram of random values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Boxplot
data =[np.random.normal(0,5, 100)]
plt.boxplot(data)
plt.title("Box plot of random values")
plt.xlabel("Data Distribution")
plt.ylabel("Values")
plt.show()