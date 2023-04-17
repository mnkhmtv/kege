for a in range(0, 500):
    pr = 1
    for x in range(0, 500):
        for y in range(0, 500):
            pr *= (x >= 9) or (2 * x < y) or (x * y < a)
            if pr == 0:
                break
    if pr == 1:
        print(a)
        break