# Week 6 Assigment 1
#
# Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to 
# https://www.py4e.com/code3/json2.py
# The program will prompt for a URL, read the JSON data from that URL using urllib and
# then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give 
# you the sum for your testing
# and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1085562.json

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1 : break

    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()

    info = json.loads(data)

    number_sum = 0

    lst = info["comments"]

    for item_dict in lst :
    	number_sum = number_sum + int(item_dict['count'])

    print('Sum:', number_sum)


    