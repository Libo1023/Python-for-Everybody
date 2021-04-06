# Week 5 Assignment
#
# Extracting Data from XML
#
# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py
# The program will prompt for a URL, read the XML data from
# that URL using urllib and then parse and extract the comment counts 
# from the XML data, compute the sum of the numbers in the file.
# 
# We provide two files for this assignment. One is a sample file
# where we give you the sum for your testing and the other is the 
# actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1085561.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())

    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    number_sum = 0

    for item in lst :
    	number_sum = number_sum + int(item.find('count').text)

    print('Sum:', number_sum)




    