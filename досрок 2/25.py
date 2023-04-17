s = '0123456789'
x = [str(i) for i in range(10)]
x += ['']
need = []
for i1 in s:
    for i2 in s:
        for i3 in x:
            res = int('11' + i1 + i2 + '4' + i3 + '56')
            if res % 211 == 0:
                need += [[res, res // 211]]

need.sort()
for i in need:
    print(*i)