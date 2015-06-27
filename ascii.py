from PIL import Image
import os

def clean_file_input():
	while True:
		ext_list = ["jpg", "jpeg", "png", "bmp"]
		name = raw_input("File Name > ")
		try:
			ext = name.split('.')[1]
		except:
			print "File needs extension"
			return False
		if name in os.listdir(".") and ext in ext_list:
			return name
		else:
			print "Invalid filename"

def to_ascii(im_name):
	out_list = []
	imag = Image.open(im_name)
	old_w, old_h = imag.size
	ratio = float(old_w) / float(old_h)
	imag = imag.resize((int(ratio*60), 60))
	conv = imag.convert("RGB")
	pix = conv.load()
	width, height = conv.size
	for Y in xrange(0, height):
		list = []
		for X in xrange(0, width):
			R, G, B = pix[X, Y]
			avg = (R + G + B)/3
			if avg < 60:
				list.append(0)
			elif avg < 120:
				list.append(1)
			elif avg < 180:
				list.append(2)
			else:
				list.append(3)
		out_list.append(list)


	for i in out_list:
		for j in i:
			if j == 3:
				print " ",
			elif j == 2:
				print ".",
			elif j == 1:
				print "%",
			elif j == 0:
				print "#",
		print

im_name = clean_file_input()
if im_name:
	to-ascii(im_name)
