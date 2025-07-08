import time

# Record start time
start = time.time()

# Code to measure
names = ["James", "Peter", "John", "Isaac"]
for name in names:
    print(name)

# Record end time
end = time.time()

execution_time = end - start
print(f"Execution time: {execution_time: .5f} seconds")

