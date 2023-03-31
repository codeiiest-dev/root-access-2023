from PIL import Image
import qrcode  
import random

flag_image = qrcode.make("accessdenied{50_y0u_4r3_600d_w17h_1m4635}")

flag_image.save("flag.png")
flag = Image.open("flag.png")

# Get the size of the images
width, height = flag.size

# Create a new black and white image to store the image1
image1 = Image.new("RGB", (width, height), "black")
image2 = Image.new("RGB", (width, height), "black")

image1 = image1.convert("1")
image2 = image2.convert("1")

def get_random_pixel():
    return random.randint(0, 1)*255

# Perform XOR on each pixel and store the image1 in the new image
for x in range(width):
    for y in range(height):
        pixel1 = flag.getpixel((x, y))
        pixel2 = get_random_pixel()
        # print(pixel1, end=" ")
        image1_pixel = pixel1 ^ pixel2
        image1.putpixel((x, y), image1_pixel)
        image2.putpixel((x, y), pixel2)

# Save the image1 as a new image file
image2.save("image1.png")
image1.save("image2.png")
