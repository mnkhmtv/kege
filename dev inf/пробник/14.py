s = '0123456789ABCDE'
for x in s:
    res = int('67845' + x + '65', 15) + int('1' + x + '23456', 15)
    if res % 14 == 0:
        print(res//14)