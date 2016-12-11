fname = input("Please enter file name: ")
file = open(fname)

for line in file:
   if line.startswith("X-DSPAM-Confidence:"):
       line = line.rstrip()
       print (line)
   