for a in range(1000):
    pr = 1
    for x in range(500):
        pr *= ((x & 52 != 0) and (x & 36 == 0)) <= (not(x & a == 0))
        if pr == 0:
            break
    if pr == 1:
        print(a)
        break