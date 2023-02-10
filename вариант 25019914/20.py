# PVPV + 2 / * 3  >=52  1)5 2) 1 <= s <= 46
def f(x, y, p):
    if (x + y) >= 52 and p == 3:
        return 1
    if (x + y) >= 52 and p < 3:
        return 0
    if (x + y) < 52 and p == 3:
        return 0
    if p % 2 == 0:
        return f(x + 2, y, p + 1) or f(x * 3, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 3, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x * 3, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 3, p + 1)

for s in range(0, 47):
    if f(5, s, 0):
        print(s)