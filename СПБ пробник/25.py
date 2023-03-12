a = [str(i) for i in range(1000)]
a += ['']
s = '0123456789'
need = []

for i in a:
    for j in s:
        res = int('1' + j + '2139' + i + '4')
        if res % 3052 == 0:
            need += [[res, res // 3052]]

need.sort()
for i in need:
    print(i)