for a in range(0, 500):
    pr = 1
    for x in range(1, 500):
        pr *= ((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)
        if pr == 0:
            break
    if pr == 1:
        print(a)
        break