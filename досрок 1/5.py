for i in range(1, 1000):
    n = bin(i)[2:]
    d = (i % 3) * 3
    if i % 3 == 0:
        n1 = n + n[-3:]
    else:
        n1 = n + bin(d)[2:]
    res = int(n1, 2)
    if res < 100:
        print(i)