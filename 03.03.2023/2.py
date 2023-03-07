from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    res = (((not(z)) <= x) and (y <= w)) <= ((w and (not(z))) or (x == y))
    if res == 0:
        print(x, y, z, w)