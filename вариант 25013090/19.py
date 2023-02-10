#  +2 / *3 s = 15
def f(s, n, p):
    if p == 2 and s >= n:
        return n
    elif p == 2 and s < n:
        return 0
    elif p < 2 and s >= n:
        return 0
    if p % 2 != 0:
        return f(s + 2, n, p + 1) or f(s * 3, n, p + 1)
    else:
        return f(s + 2, n, p + 1) and f(s * 3, n, p + 1)

for i in range(17, 1000):
    if f(15, i, 0) != 0:
        print(f(15, i, 0))