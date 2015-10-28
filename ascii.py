from PIL import Image
import os

def clean_file_input():
	while True:
		ext_list = ["jpg", "jpeg", "png", "bmp"]
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
	out_list = []
	imag = Image.open(im_name)
	old_w, old_h = imag.size
	ratio = float(old_w) / float(old_h)
	imag = imag.resize((int(ratio*size), size))
	conv = imag.convert("RGB")
	pix = conv.load()
	width, height = conv.size
	for Y in list(range(0, height)):
		appendList = []
		for X in list(range(0, width)):
			R, G, B = pix[X, Y]
			avg = (R + G + B)/3
			if avg < 60:
				appendList.append(0)
			elif avg < 120:
				appendList.append(1)
			elif avg < 180:
				appendList.append(2)
			else:
				appendList.append(3)
		out_list.append(appendList)
	return out_list

def print_ascii(out_list):
	for i in out_list:
		for j in i:
			if j == 3:
				print(" ")
			elif j == 2:
				print(".")
			elif j == 1:
				print("%")
			elif j == 0:
				print("#")
		print

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

im_name = clean_file_input()
if im_name:
	ascii = to_ascii(im_name, 160)
   
print_ascii(ascii)