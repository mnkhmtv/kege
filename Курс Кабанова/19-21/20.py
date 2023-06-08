# PVPV | +1/+4/*3 | >= 55 | 1 <= s <= 54
# 20
def f(x, p):
    if x >= 55 and p == 3:
        return 1
    if x >= 55 and p < 3:
        return 0
    if x < 55 and p == 3:
        return 0
    
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 3, p + 1)
    
for s in range(1, 55):
    if f(s, 0):
        print(s)
