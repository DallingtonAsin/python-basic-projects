from basics.modules.area import circle, rectangle
import basics.modules.colors as colors
from datetime import date


print(f"The area of the circular ring is {circle(5)}")
print(f"The area of the basketball court is {rectangle(5, 6)}")

# The built-in help() function provides a summary of a module's functions and data

delta = date(2025, 7, 3)- date(1996, 11, 16)
print("I am", delta.days // 365, "years", delta.days % 365, "days old")
print()

print(help(colors))
print(help(colors.darken))