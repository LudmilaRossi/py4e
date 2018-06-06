import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

"""
    print(data.decode())

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
"""
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    # extract all the comment/count values from the url and get the sum of all of them
    # http://py4e-data.dr-chuck.net/comments_86507.xml

    # get the content of the url as a string
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    # transform the string content into a xml tree
    # find all count elements
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment/count')
    print('Count:', len(lst))

    # extract the value of each count element and add it to the total
    total = 0
    for item in lst:
        total = total + int(item.text)
    print('Sum:', total)
