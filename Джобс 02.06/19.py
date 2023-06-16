# PVPV | -5 //3 
def f(x, p):
    if p == 2 and x <= 0:
        return 1
    if p == 2 and x > 0:
        return 0
    if p < 2 and x <= 0:
        return 0
    
    if p % 2 != 0:
        if x >= 5:
            return f(x - 5, p + 1) or f(x // 3, p + 1)
        elif 3 <= x < 5:
            return f(x // 3, p + 1)
        return 1
    else: 
        if x >= 5:
            return f(x - 5, p + 1) and f(x // 3, p + 1)
        elif 3 <= x < 5:
            return f(x // 3, p + 1)
        return 0

for s in range(5, 100):
    if f(s, 0):
        print(s)