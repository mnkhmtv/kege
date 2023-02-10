a = []
for i in range(1, 1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n1 = '1' + n[2:] + '0'
    else:
        n1 = '11' + n[2:] + '1'
    
    res = int(n1, 2)
    if res > 25:
        a += [[res, i]]

a.sort()
print(a)