#  +2 / *3 s = 15
def f(s, n, p):
    if (p == 2 or p == 4) and s >= n:
        return n
    elif (p == 2 or p == 4) and s < n:
        return 0
    elif p < 4 and s >= n:
        return 0
    if p % 2 != 0:
        return f(s + 2, n, p + 1) or f(s * 3, n, p + 1)
    else:
        return f(s + 2, n, p + 1) and f(s * 3, n, p + 1)

for i in range(16, 1000):
    if f(5, i, 0) != 0:
        print(f(5, i, 0))

print('-----------')

def f1(s, n, p):
    if p == 2 and s >= n:
        return n
    elif p == 2 and s < n:
        return 0
    elif p < 2 and s >= n:
        return 0
    if p % 2 != 0:
        return f1(s + 2, n, p + 1) or f1(s * 3, n, p + 1)
    else:
        return f1(s + 2, n, p + 1) and f1(s * 3, n, p + 1)

for i in range(7, 17):
    if f1(5, i, 0) != 0:
        print(f1(5, i, 0))