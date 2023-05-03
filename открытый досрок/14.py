s = '0123456789ABCDE'
for i in s:
    res = int('97968' + i + '15', 15) + int('7' + i + '233', 15)
    x = int(i, 15)
    if res % 14 == 0:
        print(x,res, res // 14)