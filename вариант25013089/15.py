for a in range(500, 1, -1):
    pr = 1
    for x in range(1,500):
        for y in range(1,500):
            
            pr *= ((2*y + 3*x) != 135) or (y > a) or (x > a)

    if pr == 1:
        print(a)
