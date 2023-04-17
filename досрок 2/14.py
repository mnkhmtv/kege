s = '0123456789ABCDE'
minx = 1e9
need = []
for x in s:
    r = int('97968' + x + '15', 15) + int('7' + x + '233', 15)
    if r % 14 == 0:
        need += [[int(x, 15), r // 14]]
        minx = min(minx, int(x, 15))

for i in need:
    if i[0] == minx:
        print(i[1])
        break