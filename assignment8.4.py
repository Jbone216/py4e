#ope romeo.txt and read it line by lines
#for each line, split into list of words, should build list of words
#For each word on each line, check to see if word is already in list
    #and if not append it
#When complete, sort and print resulting in alpha order

fname = input("Enter file name: ")
fh = open(fname)
fr = fh.read()
lst = list()     #Creating a blank list

for line in fr:
    line = line.strip()   #Strips white spaces of the lines in the test(fr)

words = fr.split()     #words is the result of the split (puts into list)
words.sort()   #sorts them, which gave duplicates of words (is, sun, the)

for w in words:     #for words in the list:
    if w not in lst:    ##if they aren't in the intial list:
        lst.append(w)   ##append the words "w" to it

print(lst)  #prints new list
