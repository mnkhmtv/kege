for a in range(0, 1000):
    pr = 1
    for x in range(0, 1000):
        pr *= (x & 39 == 0) or ((x & 11 == 0) <= (not(x & a == 0)))
        if pr == 0:
            break
    if pr == 1:
        print(a)
        break