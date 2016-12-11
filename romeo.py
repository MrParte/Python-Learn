fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
    if word in lst == False:
        lst.append(word)
        print (word)
    lst.append(words)
print (lst)

