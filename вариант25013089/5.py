for i in range(100000, 1, -1):
    n = bin(i)[2:]

    if n.count('1') % 2 == 0:
        n1 = n + '1'
    else:
        n1 = n + '0'

    if n1.count('1') % 2 == 0:
        n2 = n1 + '1'
    else:
        n2 = n1 + '0'

    res = int(n2, 2)

    if res < 171:
        print(i)