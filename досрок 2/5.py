for i in range(1, 500):
    n = bin(i)[2:]
    if i % 3 == 0:
        n1 = n + n[-3:]
    else:
        n1 = n + bin((i % 3) * 3)[2:]
    r = int(n1, 2)
    if r > 76:
        print(i)
        break