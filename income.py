hours = input("How many hours?")
try:
    hrs = int(hours)
except:
    hours = -1

pay = input("How much pay?")
try:
    p = float(pay)
    if hrs <= 40:
        income = hrs * p
        print (income)
    elif hrs > 40:
        income = (hrs - 40) * (1.5 * p) + 40 * p
        print (income)
except:
    pay = -1
    if hours < 0:
        print ("Pls answer in numerical value.")
    elif pay < 0:
        print ("Pls answer in numerical value.")
    else:
        print ("Thank you.")








