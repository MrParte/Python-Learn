fname = input("Please enter file name: ")
file = open(fname)
count = 0
numbercount = 0

for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
       continue
    line = line.rstrip()
    numberstart = line.find("0")
    number = line[numberstart:]
    floatnumber = float(number)
    
    count = count + 1
    numbercount = numbercount + floatnumber

average = numbercount/count
print ("Average spam confidence: ", average)


    
   