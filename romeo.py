fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if not in lst:
            lst.append()
    print (line)

