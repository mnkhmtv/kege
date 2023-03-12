for a in range(1, 1000):
    pr = 1
    for x in range(1, 16):
        pr *= ((x % 3 == 0) <= (not(x % 2 == 0))) or ((x - a) >= 4)
    if pr == 1:
        print(a)