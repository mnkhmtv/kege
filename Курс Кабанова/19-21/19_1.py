# PVPV | +1/*2 | >= 59 | 1)5 2) 1 < s < 53

def f(x, y, p):

    if (x + y) >= 59 and p == 1:
        return 1
    if (x + y) < 59 and p == 1:
        return 0
    
    return f(x + 1, y, p + 1) or f(x * 2, y, p + 1)\
    or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)

for s in range(2, 53):
    if f(5, s, 0):
        print(s)
        break