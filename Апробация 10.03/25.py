s = '0123456789'
a = [str(i) for i in range(10)]
a += ['']
need = []
for i in a:
    for j in s:
        res = int('2' + i + '5443' + j + '1')
        if res % 23 == 0:
            need += [[res, res // 23]]
need.sort()
for i in need:
    print(*i)