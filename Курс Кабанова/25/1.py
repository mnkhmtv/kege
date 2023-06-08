def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(x // i)
            d.add(i)
        if len(d) > 2:
            d = ()
            break
    if len(d) == 2:
        return list(d)

ans = []
for i in range(174_457, 174_506):
    d = div(i)
    if d != None:
        ans += [[d[0]*d[1], sorted(d)]]

ans.sort()
for i in ans:
    print(*i[1])