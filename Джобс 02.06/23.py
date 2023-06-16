def f(x, s):
    if x < s or x == 22:
        return 0
    if x == s:
        return 1
    if x > s:
        return f(x - 2, s) + f(x // 2, s) + f(x // 3, s)
print(f(40, 2))