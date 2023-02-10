# PVPV + 2 / * 3  >=52  1)5 2) 1 <= s <= 46
def f(x, y, p):
    if (x + y) >= 52 and p == 2:
        return 1
    elif (x + y) >= 52 and p < 2:
        return 0
    elif (x + y) < 52 and p == 2:
        return 0

    return f(x + 2, y, p + 1) or f(x * 3, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 3, p + 1)

for s in range(1, 47):
    if f(5, s, 0):
        print(s)