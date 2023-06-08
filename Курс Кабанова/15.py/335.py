for a in range(500, 1, -1):
    pr = 1
    for x in range(1, 500):
        for y in range(1, 500):
            pr *= (y - x ** 2 != -80) or (a < 13 * x - 14) or (a < y ** 2 + 15)
            if pr == 0:
                break
    if pr == 1:
        print(a)
        break