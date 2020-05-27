import urllib.request
import urllib.parse
import urllib.error
import re
from bs4 import BeautifulSoup
import ssl

# http://py4e-data.dr-chuck.net/known_by_Fikret.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()a
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')
reps = input('Enter Count:')
position = input('Enter Position:')
count = 0

while (count + 1) <= int(reps): #Counts as reps increase tp the input
    position = int(position) #convert user inputs to INT
    reps = int(reps)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') #get all the tags
    url = (tags[position - 1]).get('href', None)
    count = count + 1 #Counts reps

print(url)
