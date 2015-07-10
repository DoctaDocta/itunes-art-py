'''
This script will
1. parse an iTunes Library XML file
2. search and store the albums which don't have artwork
3. Search Google Images and download a photo.
4. Insert the photo as the album's artwork thru
    a. placing it in a media folder?
    b. using itunes developer api?
'''
# read Itunes Music Library.xml

# Attempt 1
'''
import xml.etree.cElementTree as etree

tree = etree.parse('/users/drfunkenstein/music/itunes/itunes music library.xml')
root = tree.getroot()

rootchildren = root.getchildren()
'''

# Attempt 2
'''
import plistlib

itunesDict = plistlib.readPlist("/users/drfunkenstein/music/itunes/itunes music library.xml");


for pppp in itunesDict['Tracks'] in range(100):
    print itunesDict['Tracks']
'''

#
import urllib2
import json as simplejson
from PIL import Image
import cStringIO

fetcher = urllib2.build_opener()
searchTerm = 'Andre'
startIndex = 0
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)

imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
file = cStringIO.StringIO(urllib2.urlopen(imageUrl).read())
img = Image.open(file)
img.save('testimg2.png')

