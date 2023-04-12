s = '0123456789'
a = [str(i) for i in range(10)]
a += ['']
need = []
for i in s:
    for j in s:
        for g in a:
            res = int('12' + i + j + '36' + g + '1')
            if res % 273 == 0:
                need += [[res, res // 273]]
need.sort()
for i in need:
    print(*i)

