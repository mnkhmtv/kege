from fnmatch import *

def sum_div(x):
    s = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x//i)
    return sum(list(s))

ans = []
for i in range(500_000, 600_000):
    sd = sum_div(i)
    if fnmatch(str(sd), '*7?'):
        ans.append([i, sd])
    if len(ans) == 5:
        break

for i in ans:
    print(*i)
