#Open and read text
#Extract integers usinf findall.() looking for [0-9]
#Convert extracted strings to integers and summ the integers

import re
fh = open('regex_sum_505432.txt')
numlist = []

for line in fh:
    line = line.strip()
    numb = re.findall('([0-9]+)', line)

    for items in numb:
        if items not in numlist:
            numlist.append(int(items))

print(sum(numlist))
