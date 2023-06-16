from fnmatch import *
def pr_mn(x):
    s = []
    d = 2
    while d ** 2 <= x:
        if x % d == 0:
            s.append(d)
            x //= d
        else:
            d += 1
    if x > 1:
        s.append(x)
    if len(s) == 7:
        return max(s)
    return 0

for i in range(1, 10 ** 4):
    mx_mn = pr_mn(i)
    if fnmatch(str(i), '*2?2') == 1 and mx_mn != 0:
        print(i, mx_mn)