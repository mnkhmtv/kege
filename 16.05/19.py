# PVPV | + 2 / + 4 / * 3 | >= 348 | 1 <= s <= 347
def f(x, p):
    if p == 2 and x >= 348:
        return 1
    if p == 2 and x < 348:
        return 0
    if p < 2 and x >= 348:
        return 0
    return f(x + 2, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)

for s in range(1, 347):
    if f(s, 0):
        print(s)
        break