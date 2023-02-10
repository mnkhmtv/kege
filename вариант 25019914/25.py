#10_000_000 2?1*67 /159
s1 = '0123456789'
s2 = ['']
for i in range(100):
    s2.append(str(i))

need = []
for i in s1:
    for j in s2:
        res = int('2' + i + '1' + j + '67')
        if res % 159 == 0:
            need += [[res, res // 159]]
need.sort()
for i in need:
    print(i)