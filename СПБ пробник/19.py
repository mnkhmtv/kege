#PVPV | //3  -12 | <=12 |  s>=13
def f(x, p):
    if p == 2 and x <=12: return 1
    if p == 2 and x > 12: return 0
    if p < 2 and x <= 12: return 0

    return f(x // 3, p + 1) or f(x - 12, p + 1)

for s in range(13, 10000):
    if f(s, 0):
        print(s)