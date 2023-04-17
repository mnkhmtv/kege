from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    res = (not (y and (not(x)))) and (not (x == z)) and w
    if res == 1:
        print(x, y, z, w)