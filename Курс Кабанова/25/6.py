def sr_ar_div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)
    divs = list(divs)
    if len(divs) > 0:
        return sum(divs)//len(divs)
    return 0

ans = []
for i in range(550_000, 600_000):
    F = sr_ar_div(i)
    if F % 31 == 13:
        ans.append([i, F])
    if len(ans) == 5:
        break

for i in ans:
    print(*i)