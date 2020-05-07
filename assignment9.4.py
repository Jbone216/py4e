#Read through mbox
#Figure out who sent most messages
#Look for a from line and take the 2nd word
#Python ict to count the number of times they appear
#Max loop to determine who was most committer


inp = input("Enter file:")
committer = dict()
handle = open(inp)

for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    words = line.split()

    for word in words:
        if word not in committer:
            committer[words[1]] = committer.get(words[1], 0) + 1

bigcommitter = None
committercount= None

for word, count in committer.items():
    if committercount is None or count > committercount:
       bigcommitter = word
       committercount = count

print(bigcommitter, committercount)
