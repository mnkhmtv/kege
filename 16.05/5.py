for i in range(1, 1000):
    n = bin(i)[2:]
    if n.count('1') % 3 == 0:
        n1 = n + n[:2]
    else:
        n1 = n + bin((int(n) % 3) * 3)[2:]
    r = int(n1, 2)
    if r < 60:
        print(i)