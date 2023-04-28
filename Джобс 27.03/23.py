def f(x,s):
    if x > s or x == 20:
        return 0
    if x == s:
        return 1
    if x < s:
        return f(x + 1, s) + f(x * 2, s)
print(f(1, 10)*f(10, 40))