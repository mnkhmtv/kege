#PVPV | //3  -12 | <=12 |  s>=13
def f(x, p):
    if (p == 2 or p == 4) and x <=12: return 1
    if p == 4 and x > 12: return 0
    if p < 4 and x <= 12: return 0
    if  p % 2 != 0:
        return f(x // 3, p + 1) or f(x - 12, p + 1)
    else:
        return f(x // 3, p + 1) and f(x - 12, p + 1)

n = []
for s in range(13, 10000):
    if f(s, 0):
        n += [s]

def f1(x, p):
    if p == 2 and x <=12: return 1
    if p == 2 and x > 12: return 0
    if p < 2 and x <= 12: return 0
    if  p % 2 != 0:
        return f1(x // 3, p + 1) or f1(x - 12, p + 1)
    else:
        return f1(x // 3, p + 1) and f1(x - 12, p + 1)
    
n1 = []
for s in range(13, 10000):
    if f1(s, 0):
        n1 += [s]
        
k = 0
for i in n:
    if i not in n1:
        k += 1
print(k)