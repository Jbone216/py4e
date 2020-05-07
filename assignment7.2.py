#Prompts filename
#opens file
#reads file
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Need to count lines and extract float val and compute the average
# Do not use sum fx or variable named sum in soltion


fname = input("Enter file name: ")
fh = open(fname)
count = 0  #Count is number of lines with spam
totalvalue = 0 #


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = (count + 1)
    value = float(line[21:]) #Slice from '0.' and on to give number
    totalvalue = value + totalvalue #Adds the values together to give a total

average = totalvalue/count #Total number after code runs / by the number of lines (count)

print('Average spam confidence:', average)
