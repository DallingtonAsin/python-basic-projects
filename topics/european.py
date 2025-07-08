from modules import conversion

# How fast were you driving? 180
# Woah, that's like 112 mph!
# What was the temperature? 35
# That's 95 degrees Fahrenheit!

print(__name__)

distance = float(input("How fast were you driving? "))
print(f"Woah, that's like {round(conversion.km2mi(distance))} mph!")

temp = float(input("What was the temperature? "))
print(f"That's {round(conversion.cel2fah(temp))} degrees Fahrenheit!")