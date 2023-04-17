for i in range(4, 500):
    s = '3' + i * '5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    summ = s.count('5') * 5 + s.count('3') * 3 + s.count('2') * 2
    if summ == 17:
        print(i)
        break