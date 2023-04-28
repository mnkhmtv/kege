maxx = 0
for i in range(1, 100):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n1 = '11' + n[2:] + '00'
    else:
        n1 = '10' + n[2:] + '11'
    if n1.count('1') % 2 == 0:
        n2 = '11' + n1[2:] + '00'
    else:
        n2 = '10' + n1[2:] + '11'
    maxx = max(int(n2, 2), maxx)

print(maxx) 