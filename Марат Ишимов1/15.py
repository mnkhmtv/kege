for a in range(1, 1000):
    pr = 1
    for x in range(1, 1000):
        pr *= ((x % 3 == 0) <= (not(x % 17 == 0))) or (not(a < 190 - x))
        if pr == 0:
            break
    if pr == 1:
        print(a)
        break