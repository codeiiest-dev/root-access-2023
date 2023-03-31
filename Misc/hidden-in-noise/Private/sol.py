from PIL import Image, ImageFilter
import cv2

# Open the two input image files
image1 = Image.open("image1.png")
image2 = Image.open("image2.png")

# Get the size of the images
width, height = image1.size

# Create a new image to store the result
result = Image.new("RGB", (width, height), "black")

# Perform XOR on each pixel and store the result in the new image
for x in range(width):
    for y in range(height):
        pixel1 = image1.getpixel((x, y))
        pixel2 = image2.getpixel((x, y))
        result_pixel = tuple([pixel1 ^ pixel2])
        result.putpixel((x, y), result_pixel)


result = result.filter(ImageFilter.GaussianBlur(radius=1))

result.save("result.png")
result.show()

# Open the result image file and scan the qrcode
def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return
    
print(read_qr_code("result.png"))