a = int(input("enter a value: "))


def factorial(a):
    res = 1
    if a == 0:
        return res
    elif a == 1:
        return res
    else:
        res = res * a * factorial(a-1)
        return res


fact = factorial(a)
print(fact)