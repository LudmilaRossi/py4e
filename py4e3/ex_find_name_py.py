# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

"""
Data Format
The file is a table of names and comment counts. You can ignore most of the data in the file except 
for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the 
numbers.
You need to adjust this code to look for span tags and pull out the text content of the span tag, 
convert them to integers and add them up to complete the assignment.
i.e:
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        print 'TAG:',tag
        print 'URL:',tag.get('href', None)
        print 'Contents:',tag.contents[0]
        print 'Attrs:',tag.attrs
"""
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

"""
spans = soup('span')

numbers = []
for span in spans:
    numbers.append(int(span.string))

print(sum(numbers))

#------------------------------

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

l=108
i=105
n=110
e=101
"""

#-------------------------------

"""
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: R
"""

#----------------------------------
#import urllib
#from BeautifulSoup import *

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

names = []

while count > 0:                         # because of `count -= 1` below,
                                         # will run loop count times

    print ('retrieving: {0}'.format(url))  # just prints out the next web page
                                         # you are going to get

    page = urllib.urlopen(url)           # urls reference web pages (well,
                                         # many types of web content but
                                         # we'll stick with web pages)

    soup = BeautifulSoup(page)           # web pages are frequently written
                                         # in html which can be messy. this
                                         # package "unmessifies" it

    tag = soup('a')                      # in html you can highlight text and
                                         # reference other web pages with <a>
                                         # tags. this get all of the <a> tags
                                         # in a list

    name = tag[position-1].string        # This gets the <a> tag at position-1
                                         # and then gets its text value

    names.append(name)                   # this puts that value in your own
                                         # list.

    url = tag[position-1]['href']        # html tags can have attributes. On
                                         # and <a> tag, the href="something"
                                         # attribute references another web
                                         # page. You store it in `url` so that
                                         # its the page you grab on the next
                                         # iteration of the loop.
    count -= 1







