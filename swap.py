x = 5
y = 7
print("formal values of x and y",(x,y))


def swap(x, y):
    a = y
    b = x
    x = a
    y = b
    return x, y


print("new values after interchange")
print(swap(x, y))
