need = []
for i in range(1, 500):
    n = bin(i - i%4)[2:]
    if n.count('1') % 2 == 0:
        n1 = n + '0'
    else:
        n1 = n + '1'

    if n1.count('1') % 2 == 0:
        n2 = n1 + '0'
    else:
        n2 = n1 + '1'
    
    res = int(n2, 2)
    if res > 100:
        need += [res]
print(min(need))
