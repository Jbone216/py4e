#Prompt a URL
#Read XML file using urllib
#parse and extract comment counts, compute sum of numbers

# http://py4e-data.dr-chuck.net/comments_42.xml

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl
lst = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')    #Input the url
d = urllib.request.urlopen(url, context = ctx)
data = d.read()

stuff = ET.fromstring(data)  #create xml fromstring for data read
lst = stuff.findall('comments/comment')   #find all comment within comments, add to list

countsum = 0
for item in lst:
    lst = item.find('count').text    #add the counts from the 'lst'
    countsum = countsum + int(lst)   #running list of the count #s

print(countsum)
