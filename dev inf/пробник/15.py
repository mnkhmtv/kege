for a in range(500):
    pr = 1
    for x in range(500):
        pr *= ((x | 42 > 64) and (x | 34 <= 102)) <= (not(x | a < 70))
        if pr == 0:
            break
    if pr == 1:
        print(a)
        break