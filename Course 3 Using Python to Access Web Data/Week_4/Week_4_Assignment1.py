# Week 4 Assignment 1
# Scraping Numbers from HTML using BeautifulSoup
# In this assignment you will write a Python program.
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and 
# the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1085559.html (Sum ends with 55)
# You do not need to save these files to your folder
# since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment
# so only use your own data url for analysis.
# You are to find all the <span> tags in the file and 
# pull out the numbers from the tag and sum the numbers.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
counts = 0
sums = 0

for tag in tags:
    # Look at the parts of a tag
    '''
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    '''
    counts = counts + 1
    int_content = int(tag.contents[0])
    sums = sums + int_content

print('Count', counts)
print('Sum', sums)
