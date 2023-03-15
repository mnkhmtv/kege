from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    res = (x <= (not(y <= z))) or w
    if res == 0:
        print(x, y, z, w)