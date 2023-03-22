def f(x, s):
    if x < s:
        return 0
    if x == s:
        return 1
    if x > s:
        return f(x - 1, s) + f(x // 2, s)
print(f(31, 12)*f(12, 2))