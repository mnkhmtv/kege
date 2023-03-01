for i in range(1, 1000):
    n = i
    bin_n = bin(i)[2:]
    n1 = n - bin_n.count('0')
    bin_n1 = bin(n1)[2:]
    if len(bin_n1) >= 3:
        n2 = bin_n1[-3:] + bin_n1
        res = int(n2, 2)
        if res > 224:
            print(res)
            