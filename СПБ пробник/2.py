from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    res = ((x <= w) and ((not (y)) <= z)) <= ((z == w) or (w and (not(y))))
    if res == 0:
        print(x, y, z, w)