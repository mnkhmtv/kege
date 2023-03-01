maxx = 0
for a1 in range(1, 1000):
    for a2 in range(a1, 1000):
        pr = 1
        for x in range(1000):
            pr *= ((not(x % 4.5 == 0)) and (not(x % 3 == 0)) or (not(17 <= x <= 34)) or (not(a1 <= x <= a2))) and ((15 <= x <= 23) or (not(a1 <= x <= a2)))
            if pr == 0:
                break
        if pr == 1:
            maxx = max(maxx, a2 - a1)

print(maxx)
