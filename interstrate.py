period = 10
principal = float(5000.00)
amount = principal
inrate = float(0.11)
year = 0
while year <= period:
    print(round(year, 2))
    print(round(amount, 2))
    value = amount + (inrate * amount)
    year = year + 1
    amount = value
