s = '0123456789ABC'
for x in s:
    res = int('753' + x + '2', 13) + int('2' + x + '173', 13)
    if res % 12 == 0:
        print(x, res // 12 )