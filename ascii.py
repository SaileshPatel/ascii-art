from __future__ import print_function
from PIL import Image
import os
import sys

help_msg = """Usage:
    python ascii.py [image_name] [vertical_size_px]
    """

shades = ["#", "%", ".", " "]

def to_ascii(im_name, size):
    lines = []
    imag = Image.open(im_name)
    old_w, old_h = imag.size
    ratio = float(old_w) / float(old_h)
    imag = imag.resize((int(ratio*size), size))
    conv = imag.convert("RGB")
    pix = conv.load()
    width, height = conv.size
    for y in range(0, height):
        tmp = []
        for x in range(0, width):
            avg = sum(pix[x, y])/3
            idx = 3 - int((float(avg)/255)*4)
            # average aspect ratio of fonts is ~0.5
            tmp.append(shades[idx])
            tmp.append(shades[idx])
        lines.append(''.join(tmp))
    return lines

if __name__ == "__main__":
    try:
        a = to_ascii(sys.argv[1], int(sys.argv[2]))
        for line in a:
            print(line)
    except Exception as e:
        print(help_msg)
        print(e)
