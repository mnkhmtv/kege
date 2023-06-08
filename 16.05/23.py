def f(x, s):
    if x > s:
        return 0
    if x == s:
        return 1
    if x < s:
        return f(x + 1, s) + f(x * 2, s) + f(x * 3, s)

a = [i for i in range(0, 16, 2)]
k = 0
for i in a[1:]:
    if f(i, 15):
        k += f(i, 15)
print(k)