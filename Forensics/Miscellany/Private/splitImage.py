from PIL import Image

img = Image.open('frame.png')
width, height = img.size
part_width = width // 50
part_height = height // 50
for i in range(50):
    for j in range(50):
        left = j * part_width
        top = i * part_height
        right = left + part_width
        bottom = top + part_height
        part = img.crop((left, top, right, bottom))
        part.save(f'./split/random_image_{i}_{j}.png')

# combining parts, will refactor later
part_width = 6
part_height = 6
rows = 50
cols = 50
combined = Image.new('RGB', (part_width * cols, part_height * rows))
for i in range(rows):
    for j in range(cols):
        part = Image.open(f'./split/random_image_{i}_{j}.png')
        left = j * part_width
        top = i * part_height
        right = left + part_width
        bottom = top + part_height
        combined.paste(part, (left, top, right, bottom))
combined.save('combined.jpg')
