def f(x, s):
    if x < s:
        return 0
    if x == s:
        return 1
    if x > s:
        return f(x - 2, s) + f(x // 2, s)

print(f(40, 10) * f(10, 2))