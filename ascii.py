from __future__ import print_function
from PIL import Image
import os
import sys

def clean_file_input(is_py2):
    while True:
        ext_list = ["jpg", "jpeg", "png", "bmp"]
        if is_py2:
            name = raw_input("File Name > ")
        else:
            name = input("File Name > ")
        try:
            ext = name.split('.')[1]
        except:
            print("File needs extension")
            return False
        if name in os.listdir(".") and ext in ext_list:
            return name
        else:
            print("Invalid filename")

def to_ascii(im_name, size):
    shades = ["#", "%", ".", " "]
    out_list = []
    imag = Image.open(im_name)
    old_w, old_h = imag.size
    ratio = float(old_w) / float(old_h)
    imag = imag.resize((int(ratio*size), size))
    conv = imag.convert("RGB")
    pix = conv.load()
    width, height = conv.size
    for Y in range(0, height):
        appendList = []
        for X in range(0, width):
            R, G, B = pix[X, Y]
            avg = (R + G + B)/3
            if avg < 60:
                appendList.append(shades[0])
            elif avg < 120:
                appendList.append(shades[1])
            elif avg < 180:
                appendList.append(shades[2])
            else:
                appendList.append(shades[3])
        out_list.append(appendList)
    return out_list

def print_ascii(out_list):
    for row in out_list:
        for char in row:
            print(char, end="")
        print()

def ascii_to_string(out_list):
    s = ""
    for appendList in out_list:
        for item in appendList:
            if item == 3:
                s += " "
            elif item == 2:
                s += "."
            elif item == 1:
                s += "%"
            elif item == 0:
                s += "#"
        s += "\n"
    return s

if sys.version_info <= (3, 0):
    is_py2 = True
im_name = clean_file_input(is_py2)
if im_name:
    ascii = to_ascii(im_name, 160)
   
print_ascii(ascii)