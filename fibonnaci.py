i = 0
f = 0
s = 1
n = 0
for i in range(0, 10):
    if i <= 1:
        n = i
        print(n)
    else:
        n = f + s
        f = s
        s = n
        print(n)