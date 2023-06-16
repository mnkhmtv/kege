from itertools import product
for x, y, z, w in product(range(2), repeat=4):
    res = (z == (not(y))) and ((not(x)) or y) and w
    if res == 1:
        print(x, y, z, w)