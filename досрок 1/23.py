# + 1 + 2 *3 | 3 - > 18 sod 8 ne sod 13
def f(x, s):
    if x > s or x == 13:
        return 0
    if x == s:
        return 1
    if x < s:
        return f(x + 1, s) + f(x + 2, s) + f(x * 3, s)

print(f(3, 8) * f(8, 18))
