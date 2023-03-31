# Open a gif file and get all the frames and then perform OCR recognition on each frame

from PIL import Image
import pytesseract
import os
import cv2
from numpy import array

def get_all_frames(gif) :
    frames = []
    try:
        while True:
            frames.append(gif.copy())
            gif.seek(len(frames))
            # save the frame
    except EOFError:
        pass
    return frames

def save_frames(frames) :
    for i, frame in enumerate(frames):
        # Create a unique filename for each frame
        filename = f"res/frame_{i}.png"
        # Save the frame as a PNG image
        frame.save(filename, format="PNG")

def ocr_on_frames(n) :
    flag = ""
    for i in range(n) :
        img = cv2.imread(f"res/frame_{i}.png")
        # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #
        # msk = cv2.inRange(hsv, array([0, 0, 0]), array([179, 84, 255]))
        # krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
        # dlt = cv2.dilate(msk, krn, iterations=1)
        # thr = 255 - cv2.bitwise_and(dlt, msk)
        # # save thr
        # cv2.imwrite(f"res/thr_{i}.png", thr)
        # txt = pytesseract.image_to_string(img)
        txt = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}')
        # print(txt)
        flag += txt.strip()
    return flag

def main() :
    frames = get_all_frames(Image.open("flag.gif"))
    save_frames(frames)
    flag = ocr_on_frames(len(frames))
    print("Flag: ", flag)

if __name__ == "__main__" :
    main()
