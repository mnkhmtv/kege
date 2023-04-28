from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    res = ((x <= (y and w)) and (z <= (x or y))) != w
    if res == 1:
        print(x, y, z, w)