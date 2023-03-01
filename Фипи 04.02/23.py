def f(x, s):
    if x > s or x == 9:
        return 0
    elif x == s:
        return 1
    elif x < s:
        return f(x + 1, s) + f(x * 2, s)

print(f(2, 12) * f(12, 42))