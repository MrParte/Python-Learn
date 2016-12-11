hrs = input("How many hours?")
hours = float(hrs)
rte = input("What is the rate?")
rate = float(rte)

def computePay(hours, rate):
    if hours > 40:
        income = (40 * rate) + (hours - 40) * (rate * 1.5)
        return (income)
    elif hours <= 40: 
        income = hours * rate
        return (income)

print (computePay(hours, rate))

    
