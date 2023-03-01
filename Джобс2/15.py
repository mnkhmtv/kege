for a in range(1000, 1, -1):
    pr = 1
    for x in range(500):
        pr *= (a <= (43 <= x <= 49)) or (44 <= x <= 53)
    
    if pr == 1:
        print(a)
        