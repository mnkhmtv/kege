# PVPV | +1/*2 | >= 59 | 1)5 2) 1 < s < 53

def f(x, y, p):

    if (x + y) >= 59 and (p == 2 or p == 4):
        return 1
    if (x + y) < 59 and p == 4:
        return 0
    if (x + y) >= 59 and p < 4:
        return 0

    if p % 2 != 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1)\
        or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1)\
        and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)


for s in range(2, 53):
    if f(5, s, 0):
        print(s)

print('======')

def g(x, y, p):

    if (x + y) >= 59 and p == 2:
        return 1
    if (x + y) < 59 and p == 2:
        return 0
    if (x + y) >= 59 and p < 2:
        return 0

    if p % 2 != 0:
        return g(x + 1, y, p + 1) or g(x * 2, y, p + 1)\
        or g(x, y + 1, p + 1) or g(x, y * 2, p + 1)
    else:
        return g(x + 1, y, p + 1) and g(x * 2, y, p + 1)\
        and g(x, y + 1, p + 1) and g(x, y * 2, p + 1)


for s in range(2, 53):
    if g(5, s, 0):
        print(s)