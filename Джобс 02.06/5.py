for i in range(1, 500):
    n = bin(i)[2:]
    if n.count('1') % 4 == 0:
        n1 = '10' + n
    else:
        n1 = '11' + n
    if int(n1, 2) % 2 != 0:
        n2 = n1 + '0'
    else:
        n2 = n1 + '1'
    res = int(n2, 2)
    if res < 250:
        print(i)