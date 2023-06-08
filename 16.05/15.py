for a in range(0, 500):
    pr = 1
    for x in range(0, 500):
        for y in range(0, 500):
            pr *= ((2 * x + y) != 150) or (not(50 <= x <= 70)) or (a > y)
            if pr == 0:
                break
    if pr == 1:
        print(a)
        break