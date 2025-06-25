import pyfiglet
import random

def generate_fathers_day_wish():
    message = "Happy Father's Day!"
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = random.choice(fonts)
    ascii_art = pyfiglet.figlet_format(message, font=selected_font)
    return ascii_art


# Calling the function to generate the wish
fathers_day_wish = generate_fathers_day_wish()

# Printing the wish
print(fathers_day_wish)

