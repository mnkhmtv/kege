#  +2 / *3 s = 15
def f(s, n, p):
    if p == 3 and s >= n:
        return n
    elif p == 3 and s < n:
        return 0
    elif p < 3 and s >= n:
        return 0
    if p % 2 == 0:
        return f(s + 2, n, p + 1) or f(s * 3, n, p + 1)
    else:
        return f(s + 2, n, p + 1) and f(s * 3, n, p + 1)

for i in range(12, 1000):
    if f(10, i, 0) != 0:
        print(f(10, i, 0))