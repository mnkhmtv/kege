s = '0123456789ABCDEFG'
for x in s:
    res = int('G23' + x + '5', 17) + int('1' + x + '23E', 17)
    if res % 13 == 0:
        print(int(x, 17))
        print(res // 13)