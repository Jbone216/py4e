#Write a program to read through the mbox-short.txt and figure out the distribution
    #by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then
    #splitting the string a second time using a colon.
    #From ,stephen.marquard@uct.ac.za, Sat, Jan,  5, 09:14:16, 2008
#Once you have accumulated the counts for each hour, print out the counts,
    #sorted by hour as shown below.


fn = input("Enter file:")
fh = open(fn)

dct = dict()     #Create empty dicionary
lst = list()     #Create empty list

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue   #Get 'From' lines
    words = line.split()
    time = words[5].split(':') #double split per question (hour is index 5)
    hour = time [:2]   #Sliced the time to give 1st 2 digits

    #for word in time:         ###Kept getting right time, wonrg output with this.
        #if word not in dct:        ##Once i deleted loop, gave right answer
    dct[hour[0]] = dct.get(hour[0],0) + 1  #Add hours to dictionary


for k,v in dct.items():  #Add dic items to list
    lst.append((k,v))

lst.sort()     #Sort list and print

for k,v in lst:
    print(k,v)
