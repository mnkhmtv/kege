# PVPV  | +2 / +4 / *2 | >= 100 | 1 <= s <= 99 |
def f(x, p):
    if p == 4 and x >= 100:
        return 1
    if p < 4 and x >= 100:
        return 0
    if p < 4 and x < 100:
        if p % 2 != 0:
            return f(x + 2, p + 1) or f(x + 4, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x + 4, p + 1) and f(x * 2, p + 1)

for i in range(1, 100):
    if f(i, 0):
        print(i)