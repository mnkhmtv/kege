def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
        if len(d) > 4:
            d = ()
            break
    if len(d) == 4:
        return sorted(d)
    
ans = []
for i in range(154_026, 154_043):
    divid = div(i)
    if divid != None:
        ans.append(divid[2:])

ans.sort()
for i in ans:
    print(*i)
