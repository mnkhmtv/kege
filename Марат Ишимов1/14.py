s = '0123456789ABCDEFGHIJK'
s1 = '13579BDFHJ'
minx = []
min1 = []
minn = 1e9
for x in s:
    for y in s1:
        res = int('32' + y + x + 'A',21) + int('16'+ y + '18', 21)
        
        if res % 12 == 0:
            minn = min(minn, int(x, 21))
            minx += [[int(x, 21),y, res // 12]]

print(minn)
for i in minx:
    if i[0] == minn:
        print(i)

        
