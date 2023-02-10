# +1 / *2
def f(x, s):
    if x > s:
        return 0
    if x == s:
        return 1
    return f(x + 1, s) +  f(x * 2, s)

print(f(2, 7)*f(7, 16)*f(16, 39))