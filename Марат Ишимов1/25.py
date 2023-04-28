# >500_000   5 naimen   3 delit  *1?3
def delit(n):
    a = [str(i) for i in range(1, 300)]
    a += ['']
    s = '0123456789'
    need = []
    for i in a:
        for j in s:
            res = int(i + '1' + j + '3')
            need += [res]
    need = set(need)
           
    d = []
    for i in need:
        if n % i == 0:
            d += [i, n // i]
    d = set(d)
    if len(d) == 3:
        return max(d)

need = []
for i in range(500_000, 510_000):
    if delit(i):
        need += [[i, delit(i)]]
        print(need)
for i in need:
    print(i)
    input()

