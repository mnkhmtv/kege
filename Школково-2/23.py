# +1 *2 +3
def f(x, s):
    if x == 7 or x == 15 or x > s:
        return 0

    if x == s:
        return 1

    if x < s:
        return f(x + 1, s) + f(x * 2, s) + f(x + 3, s)

print(f(2, 20))
 