def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
        if len(d) > 3:
            d = ()
            break
    if len(d) == 3:
        return sorted(list(d))

ans =[]
for i in range(81_234, 134_689 + 1):
    divid = div(i)
    if divid:
        ans += [divid]

ans.sort()
for i in ans:
    print(*i)