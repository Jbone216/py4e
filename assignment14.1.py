
import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

#http://py4e-data.dr-chuck.net/comments_42.json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')    
ur = urllib.request.urlopen(url, context = ctx)
data = ur.read().decode()
info = json.loads(data)

count = 0
for item in info['comments']:
    number = int(item['count'])
    count = count + number

print(count)
