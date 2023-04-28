def f(x, s):
    if x < s:
        return 0
    if x == s:
        return 1
    if x > s:
        return f(x - 4, s) + f(x -sum(map(int, str(x))), s)
print(f(36, 14)*f(14, 2))