#PVPV +1/*2  >=25 1)4 2)1 <= s <= 20

def f(x, y, p):
    if p == 4 and (x + y) >= 25:
        return 1
    if p == 4 and (x + y) < 25:
        return 0
    if (x + y) >= 25:
        return 0
    if p % 2 != 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) \
            or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) \
            and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)

for s in range(1, 21):
    if f(4, s, 0):
        print(s)

print('---------')

def f1(x, y, p):
    if p == 2 and (x + y) >= 25:
        return 1
    if p == 2 and (x + y) < 25:
        return 0
    if (x + y) >= 25:
        return 0
    if p % 2 != 0:
        return f1(x + 1, y, p + 1) or f1(x * 2, y, p + 1) \
            or f1(x, y + 1, p + 1) or f1(x, y * 2, p + 1)
    else:
        return f1(x + 1, y, p + 1) and f1(x * 2, y, p + 1) \
            and f1(x, y + 1, p + 1) and f1(x, y * 2, p + 1)
for s in range(1, 21):
    if f1(4, s, 0):
        print(s)