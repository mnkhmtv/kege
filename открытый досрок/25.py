s = [str(i) for i in range(10)]
s.append('')
s1 = '0123456789'
need = []
for i in s1:
    for j in s1:
        for k in s:
            res = int('12' + i + j + '1' + k + '56')
            if res % 317 == 0:
                need += [[res, res//317]]
need.sort()
for i in need:
    print(*i)