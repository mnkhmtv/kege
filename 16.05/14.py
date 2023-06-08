s = '0123456789ABCDEF'
for x in s:
    r = int('1' + x + '51', 15) - int('3' + x + '2', 15)
    if r % 4 == 0:
        print(int(x, 15), r // 4)