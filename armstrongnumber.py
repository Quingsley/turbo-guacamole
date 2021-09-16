lower = int(input("enter lower limit: "))
upper = int(input("enter upper limit: "))
for number in range(lower, upper + 1):


    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if number == sum:
        print(number)

