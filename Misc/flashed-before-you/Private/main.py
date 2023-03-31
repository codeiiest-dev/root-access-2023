# Script will generate a GIF from a series of frames

import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont

flag = "accessdenied{youarefast}"
# Generate the frames
width, height = 200, 200
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)

# Generate a frame with the given character as text in img
def generate_image(char, filename):
    img = Image.new('RGB', (width, height), color = (255,255,255))
    d = ImageDraw.Draw(img)
    d.text((width/2, height/2), char, fill=(0, 0, 0), font=fnt)
    img.save(filename)

def generate_save_frames():
    for i in range(len(flag)):
        generate_image(flag[i], "frames/frame_" + str(i) + ".png")

def generate_gif():
    frames = []
    for i in range(len(flag)):
        frames.append(Image.open("frames/frame_" + str(i) + ".png"))
    frames[0].save('flag.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)

def main():
    generate_save_frames()
    generate_gif()

main()