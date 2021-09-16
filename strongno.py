def factorial(digit):
    res = 1
    if digit == 0:
        return res
    elif digit == 1:
        return res
    else:
        res = res * digit * factorial(digit-1)
        return res


lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
for n in range (lower, upper + 1):

    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + factorial(digit)
        temp //= 10

    if sum == n:
        print(str(n) + " is a strong number")

