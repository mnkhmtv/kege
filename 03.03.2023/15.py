# не получилось :(
l = 0
minl = 1e9
for a1 in range(1, 100):
    for a2 in range(a1 + 1, 101):
        pr = 1
        l = a2 - a1
        for x in range(1, 100):
            pr *= ((25 <= x <= 60) <= ((not(12 <= x <= 32)) and (25 <= x <= 60) <= (a1 <= x <= a2)))

        if pr == 1:
         
            minl = min(minl, l)
print(minl)


