s = '0123456789ABCDE'
need = []
minx = 1e9
for  x in s:
    res = int(int('97968' + x + '13', 15) + int('7' + x + '213', 15))
    if res % 14 == 0:
        need += [[int(x, 15), res//14]]
        minx = min(minx, int(x, 15))

for i in need:
    if i[0] == minx:
        print(i[1])
        input()
