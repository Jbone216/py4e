import urllib.request
import urllib.parse
import urllib.error
import re
from bs4 import BeautifulSoup
import ssl
numlist = []

# http://py4e-data.dr-chuck.net/comments_505434.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('tr')

for line in tags:
    line = line.decode().strip()
    numb = re.findall('([0-9]+)', line)
    if not line.startswith('<tr>'): continue
    for items in numb:
        if items not in numlist:
            numlist.append(int(items))

print(sum(numlist))
