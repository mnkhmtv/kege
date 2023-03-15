#PVPV | +1/+4/*2 | >=351 | 1 <= s <= 350

def f(x, p):
    if p == 2 and x >= 351: return 1
    if p == 2 and x < 351: return 0
    if p < 2 and x >= 351: return 0

    if p % 2 != 0:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 2, p + 1)

for s in range(1, 351):
    if f(s, 0):
        print(s)