fname = input("Please enter file name: ")
file = open(fname)

for line in file:
    line = line.rstrip()
    line = line.upper()
    print (line)
