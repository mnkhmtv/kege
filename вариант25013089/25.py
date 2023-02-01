# 12*6789
a = ['']
for i in range(100):
    a.append(str(i))

need = []    
for i in a:
    res = int('12' + i + '6789')
    if res % 39 == 0:
        need += [[res, res // 39]]

need.sort()
for i in need:
    print(i)