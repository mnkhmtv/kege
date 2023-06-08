from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    r = ((not(x)) <= y) == ((x <= z) or (not(w)))
    if r == 0:
        print(x, y, z, w)
