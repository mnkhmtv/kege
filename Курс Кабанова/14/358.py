alp23 = '0123456789ABCDEFGHIJKL'
alp13 = '0123456789ABC'
need = []
for x in alp23:
    for y in alp13:
        res = int(x + '23' + x + '5', 22) - int('67' + y + '9' + y, 13)
        if abs(res) % 57 == 0:
            need += [[int(x, 23) + int(y, 13), res // 57]]
need.sort()
print(need[0][1])