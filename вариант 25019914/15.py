count = 0
for a in range(1, 500):
    pr = 1
    for x in range(1, 500):
        for y in range(1, 500):
            pr *= (x > a) or (y > a) or ((y - 2 * x  + 12) != 0)
    if pr == 1:
        count += 1

print(count)