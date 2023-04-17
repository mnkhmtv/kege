# PVPV | +1/+4/*3 | | >= 43 | 1 <= s <= 42
def f(x, p):
    if x >= 43 and p == 2:
        return 1
    if x < 43 and p == 2:
        return 0
    if x >= 43 and p < 2:
        return 0
    
    if p % 2 != 0:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 3, p + 1)

for s in range(1, 43):
    if f(s, 0):
        print('19)', s)
        break

def f1(x, p):
    if x >= 43 and p == 3:
        return 1
    if x < 43 and p == 3:
        return 0
    if x >= 43 and p < 3:
        return 0
    
    if p % 2 == 0:
        return f1(x + 1, p + 1) or f1(x + 4, p + 1) or f1(x * 3, p + 1)
    else:
        return f1(x + 1, p + 1) and f1(x + 4, p + 1) and f1(x * 3, p + 1)

for s in range(1, 43):
    if f1(s, 0):
        print('20)',s)

def f12(x, p):
    if x >= 43 and (p == 2 or p == 4):
        return 1
    if x < 43 and p == 4:
        return 0
    if x >= 43 and p < 4:
        return 0
    
    if p % 2 != 0:
        return f12(x + 1, p + 1) or f12(x + 4, p + 1) or f12(x * 3, p + 1)
    else:
        return f12(x + 1, p + 1) and f12(x + 4, p + 1) and f12(x * 3, p + 1)

for s in range(1, 43):
    if f12(s, 0):
        print('1)', s)

print('---')

def f123(x, p):
    if x >= 43 and p == 2:
        return 1
    if x < 43 and p == 2:
        return 0
    if x >= 43 and p < 2:
        return 0
    
    if p % 2 != 0:
        return f123(x + 1, p + 1) or f123(x + 4, p + 1) or f123(x * 3, p + 1)
    else:
        return f123(x + 1, p + 1) and f123(x + 4, p + 1) and f123(x * 3, p + 1)

for s in range(1, 43):
    if f123(s, 0):
        print('2)', s)