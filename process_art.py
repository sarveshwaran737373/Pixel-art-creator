import ast
from PIL import Image

def create_image_from_data(pixel_data_list, width, height):
    """
    Creates an image from a list of hex color strings.
    """
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    for i, color_hex in enumerate(pixel_data_list):
        x = i % width
        y = i // width
        
        # Convert hex to RGB tuple
        if color_hex.startswith('#'):
            color_hex = color_hex.lstrip('#')
            rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
            pixels[x, y] = rgb
            
    return img

# ---------------------------------------------------------
# PASTE YOUR EXPORTED DATA FROM THE HTML TOOL BELOW THIS LINE
# Example format:
# pixel_data = [
#    '#ffffff', '#ffffff', ...
# ]
# ---------------------------------------------------------

# Replace this list with the output from the HTML tool
pixel_data = [
    '#ffffff' for _ in range(256) # Placeholder: 16x16 white image
]

# If you have real data, uncomment the line below and paste your data in the variable above
# image = create_image_from_data(pixel_data, 16, 16) 
# image.save("my_pixel_art.png")
# print("Image saved as my_pixel_art.png")

if __name__ == "__main__":
    print("Python script ready. Paste your pixel data into the script variable 'pixel_data' and run to generate the PNG.")
    print("Note: The HTML tool exports data for a 16x16 grid (320px / 20px = 16).")
