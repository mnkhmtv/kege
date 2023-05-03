#PVPV | +1/+4/*3 | >= 43 | 1 <= s <= 42
def f1(x, p):
    if p == 2 and x >= 43:
        return 1
    if p == 2 and x < 43:
        return 0
    if p < 2 and x >= 43:
        return 0
    if p % 2 != 0:
        return f1(x + 1, p + 1) or f1(x + 4, p + 1) or f1(x *3, p + 1)
    else:
        return f1(x + 1, p + 1) and f1(x + 4, p + 1) and f1(x *3, p + 1)
for s in range(1, 43):
    if f1(s, 0): print('19)', s)

def f2(x, p):
    if p == 3 and x >= 43:
        return 1
    if p == 3 and x < 43:
        return 0
    if p < 3 and x >= 43:
        return 0
    if p % 2 == 0:
        return f2(x + 1, p + 1) or f2(x + 4, p + 1) or f2(x *3, p + 1)
    else:
        return f2(x + 1, p + 1) and f2(x + 4, p + 1) and f2(x *3, p + 1)
for s in range(1, 43):
    if f2(s, 0): print('20)', s)

def f12(x, p):
    if (p == 2 or p == 4) and x >= 43:
        return 1
    if p == 4 and x < 43:
        return 0
    if p < 4 and x >= 43:
        return 0
    if p % 2 != 0:
        return f12(x + 1, p + 1) or f12(x + 4, p + 1) or f12(x *3, p + 1)
    else:
        return f12(x + 1, p + 1) and f12(x + 4, p + 1) and f12(x *3, p + 1)
for s in range(1, 43):
    if f12(s, 0): print('21)', s)
