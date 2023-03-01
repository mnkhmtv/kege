from itertools import product
for a in range(1,500):
    pr = 1
    for x,y,z in product(range(100), repeat = 3):
        pr *= (z % 115 == 0 or y % 78 == 0 or x % 51 == 0) <= (x % a == 0)
        if pr == 0:
            break
    if pr == 1:
        print(a)