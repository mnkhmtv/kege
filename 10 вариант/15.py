for a in range(1, 500):
    pr = 1
    for x in range(1, 500):
        pr *= (not (x % a == 0)) <= ((x % 26 == 0) <= (not(x % 169 == 0)))
    if pr == 1:
        print(a)