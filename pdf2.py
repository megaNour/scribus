#!/usr/bin/env python3
import glob
import re
import os
import sys
if os.name == "nt":
	addMe = os.environ["MYPYTHONPATH"]
	sys.path.append(addMe)
import pyManga.constants2 as constants
import argparse
from os.path import splitext

parser = argparse.ArgumentParser()
parser.add_argument("-d", required=True, help="the directory the file is in")
parser.add_argument("-p", help="the page range to process as x,y,a-b,e...")

args, unknown = parser.parse_known_args()

os.chdir(args.d)
print(args.d + " 7777777777777777777")
for slaFileName in glob.glob("*.sla"):
	scribus.openDoc(slaFileName)
	print("1111111111111111111111111111111")
	if not args.p:
		if os.path.isfile("sequence.txt"):
			file = open("sequence.txt", "r")
			args.p = file.readline().replace(" ", ",").strip()
			file.close()
			print("1111111111111111111111111111112")
		else:
			args.p = "1-" + str(pageCount())
			print("1111111111111111111111111111113")
	elif not os.path.isfile("sequence.txt"):
		file = open("sequence.txt", "w")
		file.write(args.p.replace(",", " "))
		file.close()
		print("1111111111111111111111111111114")
	for scroll in args.p.split(","):
		print("1111111111111111111111111111115")
		print("scroll: " + scroll)
		pdf = scribus.PDFfile()
		pdf.file = splitext(slaFileName)[0] + "_p" + constants.zfillParamString(scroll, 2) + ".pdf"
		pdf.binding = 1 #RIGHT TO LEFT
		pdf.compress = True
		pdf.pages = constants.listString(scroll)
		pdf.pages.sort()
		pdf.compressmtd = 3 #NONE
		pdf.resolution = 300
		print("############################################")
		print(scroll + " printing pages: " + str(pdf.pages))
		pdf.save()

