def delit(n):
    d = []
    for i in range(2, int(n**0.5) + 1):
        if i * i == n:
            d += [i]
        elif n % i == 0:
            d += [i, n // i]
    if len(d) >= 2:
        return max(d) - min(d)
    else:
        return 0
need = []
for n in range(850_000, 1_000_000):
    f = delit(n)
    if f != 0 and f % 5 == 0 and len(need) <= 6:
        need += [[n, f]]
        if len(need) == 6:
            break

for i in need:
    print(*i)

            