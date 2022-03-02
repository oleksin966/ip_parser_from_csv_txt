#!/usr/bin/python
import re
import sys
import csv

def parse():
	lst = []
	with open(sys.argv[1],errors='ignore') as f:
		if sys.argv[1].endswith(".txt"):
			fstrings_txt = f.readlines()
			for i in range(len(fstrings_txt)):
				if (fstrings_txt[i].startswith("192") == False or \
					fstrings_txt[i].startswith("17") == False or
					fstrings_txt[i].startswith("255") == False or 
					fstrings_txt[i].startswith("10") == False):
					pattern = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str(fstrings_txt[i]), re.M|re.I)
					if pattern:
						lst.append(pattern.group(1))
		elif sys.argv[1].endswith(".csv"):
			csvreader = csv.reader(f)
			header = next(csvreader)
			for row in csvreader:
				lst.append(row[0].split(";")[0])
	return (set(lst))

def save_ip(ips):
	f = open(sys.argv[2], 'w')
	for k in ips:
		f.write(str(k) + "\n")
	f.close()

save_ip(parse())
