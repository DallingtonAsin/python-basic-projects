from rembg import remove
from PIL import Image


try: 
    input_path="/home/dallington/Desktop/Chevening/pic.jpg"
    output_path="/home/dallington/Desktop/Chevening/formatted/pic.png"
    
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    print("Done successfully")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
