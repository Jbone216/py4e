#Open file and read it line by lines
#When you find a line that starts with From, parse the line using
    #split and print out the second word in the line, which is entire
    #address of person who sent it.
#Print a count at the end
#Hint: Make sure to not include the lines that start with From


fname = input("Enter file name: ")


fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    word = line.split()
    count = count + 1
    print(word[1])


print("There were", count, "lines in the file with From as the first word")
