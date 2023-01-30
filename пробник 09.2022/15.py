for a in range(1,10000):
    pr = 1
    for x in range(1,10000):
        res = ((x%6==0) <= (x%10!=0)) or (x + a > 121)
        if res == 0:
            pr = 0
            break
    if pr == 1:
        print(a)
        input()
