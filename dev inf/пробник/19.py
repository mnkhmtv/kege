# PVPV | x: *2 y: +3/+4 | > 14 ed | (3; s) 1 <= s <= 13
def f(x, y, p):
    d = (x ** 2 + y ** 2) ** 0.5
    if p == 2 and d > 14:
        return 1
    if p == 2 and d <= 14:
        return 0
    if p < 2 and d > 14:
        return 0
    
    if p % 2 != 0:
        return f(2 * x, y, p + 1) or f(x, y + 3, p + 1) or f(x, y + 4, p + 1)
    else:
        return f(2 * x, y, p + 1) and f(x, y + 3, p + 1) and f(x, y + 4, p + 1)
    
for s in range(1, 14):
    if f(3, s, 0):
        print(s)