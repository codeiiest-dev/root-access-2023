from PIL import Image
import numpy as np

def disrupt_even(image):
    height, width , channels= image.shape
    for x in range(height):
        for y in range(0,width//2):
            if((y%2) == 0):
                r , g , b = image[x,y]
                image[x,y,0] = image[x,width-y - 1,1]
                image[x,y,1] = image[x,width-y - 1,2]
                image[x,y,2] = image[x,width-y - 1,0]
                image[x,width-y - 1,0] = g
                image[x,width-y - 1,1] = b
                image[x,width-y - 1,2] = r
    for x in range(0,height//2):
        for y in range(width):
            if((x%2) == 0):
                r , g , b = image[x,y]
                image[x,y,0] = image[height - x - 1,y,1]
                image[x,y,1] = image[height - x - 1,y,2]
                image[x,y,2] = image[height - x - 1,y,0]
                image[height - x - 1,y,0] = g
                image[height - x - 1,y,1] = b
                image[height - x - 1,y,2] = r
    return image

def disrupt_even_reverse(image):
    height, width , channels= image.shape
    for x in range(0,height//2):
        for y in range(width):
            if((x%2) == 0):
                r , g , b = image[x,y]
                image[x,y,0] = image[height - x - 1,y,2]
                image[x,y,1] = image[height - x - 1,y,0]
                image[x,y,2] = image[height - x - 1,y,1]
                image[height - x - 1,y,0] = b
                image[height - x - 1,y,1] = r
                image[height - x - 1,y,2] = g
    for x in range(height):
        for y in range(0,width//2):
            if((y%2) == 0):
                r , g , b = image[x,y]
                image[x,y,0] = image[x,width-y - 1,2]
                image[x,y,1] = image[x,width-y - 1,0]
                image[x,y,2] = image[x,width-y - 1,1]
                image[x,width-y - 1,0] = b
                image[x,width-y - 1,1] = r
                image[x,width-y - 1,2] = g
    return image

def readImage(inputImg):
    image = np.array(Image.open(inputImg))
    image = disrupt_even(image)
    disrupted_image = Image.fromarray(image)
    disrupted_image.save('disrupted_image.png')

def decryptImage(inputimg):
    image = np.array(Image.open(inputimg))
    image = disrupt_even_reverse(image)
    disrupted_image = Image.fromarray(image)
    disrupted_image.save('retrieved.png')

readImage("image.png")
decryptImage("myArt.png")