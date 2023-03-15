n = []
for a in range(0, 500):
    pr = 1
    for x in range(1, 500):
        for y in range(1, 500):
            if ((x + y <= 32) or (y <= x + 4) or (y >= a)) == 0:
                pr = 0
                break
    if pr == 1:
        n += [a]
print(max(n))