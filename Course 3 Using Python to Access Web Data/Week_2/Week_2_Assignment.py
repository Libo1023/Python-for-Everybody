# Week 2 Assignment
# Extracting Data with Regular Expressions
# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re
hand = open('regex_sum_1085557.txt')
numlist = list()

for line in hand :
	line = line.rstrip()
	stuff = re.findall('[0-9]+', line)

	for number_string in stuff :
		number_float = float(number_string)
		numlist.append(number_float)

print(int(sum(numlist)))