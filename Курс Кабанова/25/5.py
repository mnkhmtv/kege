def sum_divs(x):
    divs = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)
    
    if len(divs) > 1:
        divs = sorted(list(divs))
        return divs[0] + divs[-1]
    return 0 

ans = []
for i in range(250_200, 300_000):
    S = sum_divs(i)
    if S % 123 == 17:
            ans.append([i, S])
    if len(ans) > 4:
         break

for i in ans:
     print(*i)

