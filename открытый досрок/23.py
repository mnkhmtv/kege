def f(x, s):
    if x > s or x == 15:
        return 0
    if x == s:
        return 1
    if x < s:
        return f(x + 1, s) + f(x * 2, s) + f(x * 3, s)

print(f(1, 11) * f(11, 25))