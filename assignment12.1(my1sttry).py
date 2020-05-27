#Use urllib to read the HTML
#parse the data
#Extract the numbers and compute the sum of the numbers in the Files
#Data Format: Table of names and comment counts, ignore most of data aside from:
  #<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#Find all the <span> tags and pull out the numbers and sum SectionAwareServiceHelperImpl
#Loop through the tags
  #Adjust code to loop for span tags and pull text content out of tag, convert to
    #int

import urllib.request
import re
import bs4

numlist = []
fh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_505434.html')
soup = BeautifulSoup(html, 'html.parser')

for line in fh:
    line = line.decode().strip()
    numb = re.findall('([0-9]+)', line)
    if not line.startswith('<tr>'): continue
    for items in numb:
        if items not in numlist:
            numlist.append(int(items))

print(sum(numlist))
