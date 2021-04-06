# Week 4 Assignment 2
# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= vaues 
# from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find.
# We provide two files for this assignment.
# One is a sample file where we give you the name for your testing and the other is the actual 
# data you need to process for the assignment.
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Qirui.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
count_string = input('Enter count: ')
position_string = input('Enter position: ')


'''
url = 'http://py4e-data.dr-chuck.net/known_by_Qirui.html'
count_string = '7'
position_string = '18'
'''

count = int(count_string)
position = int(position_string)

count_flag = 0
names = list()

while (count_flag < count) :
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	tags = soup('a')

	position_flag = 1

	for tag in tags :
		if (position_flag == position) :
			url = tag.get('href', None)
			names.append(tag.contents[0])

			print(url)

			position_flag = 1
			break
		else :
			position_flag = position_flag + 1

	count_flag = count_flag + 1

print('The correct name is:', names[len(names)-1])
# print(names)




