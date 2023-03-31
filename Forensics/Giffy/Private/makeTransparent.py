# -*- coding: utf-8 -*-
from PIL import Image

for i in range(445):
    img = Image.open('shit/frame_{}_delay-0.2s.gif'.format(str(i).rjust(3, '0')))
    img = img.convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)
    img.save("Solution2/{}.png".format(i), "PNG")