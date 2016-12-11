hours = input("How many hours?")
hrs = int(hours)

pay = input("How much pay?")
p = float(pay)

if hrs < 40:
    income = hrs * p
    print (income)
elif hrs > 40:
    income = (hrs - 40) * (1.5 * p) + 40 * p
    print (income)