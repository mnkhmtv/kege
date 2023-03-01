for i in range(1, 1000):
    n = bin(i)[2:]

    n1 = n + n[-1]

    if n1.count('1') % 2 == 0:
        n2 = n1 + '0'
    else:
        n2 = n1 + '1'

    if n2.count('1') % 2 == 0:
        n3 = n2 + '0'
    else:
        n3 = n2 + '1'
    
    res = int(n3, 2)

    if res > 97:
        print(i)