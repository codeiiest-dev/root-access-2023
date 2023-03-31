from PIL import Image
import base64

def encode_text_in_image(image_path, text_to_hide):
    string_to_encode = text_to_hide
    bytes_to_encode = string_to_encode.encode('utf-8')
    base64_encoded_bytes = base64.b64encode(bytes_to_encode)
    base64_encoded_string = base64_encoded_bytes.decode('utf-8')
    image = Image.open(image_path)
    ascii_codes = [ord(char) for char in base64_encoded_string]
    binary_text = ''.join([format(code, '08b') for code in ascii_codes])
    width, height = image.size
    pixels = image.load()
    index = 0
    for row in range(height):
        for col in range(width-1,width):
            r, g, b = pixels[col, row]
            if index < len(binary_text):
                r = (r & ~1) | int(binary_text[index])
                index += 1
            if index < len(binary_text):
                g = (g & ~1) | int(binary_text[index])
                index += 1
            if index < len(binary_text):
                b = (b & ~1) | int(binary_text[index])
                index += 1
            pixels[col, row] = (r, g, b)
    image.save('megatron.png')
    
encode_text_in_image('peter.png', 'accessdenied{p3t3r_gr!ff!n_5@v35_th3_d@y}')

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()
    binary_text = ''
    for row in range(height):
        for col in range(width-1, width):
            r, g, b = pixels[col, row]
            binary_text += str(r & 1)
            binary_text += str(g & 1)
            binary_text += str(b & 1)
    ascii_text = ''
    for i in range(0, len(binary_text), 8):
        ascii_code = int(binary_text[i:i+8], 2)
        ascii_text += chr(ascii_code)
    return ascii_text

text = extract_text_from_image('megatron.png')
print(text) 