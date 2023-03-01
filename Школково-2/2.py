from itertools import product

for x, y, z, w in product(range(2), repeat = 4):
    res = ((not(x)) <= y) and (y == (not(z))) and (not(w))
    if res == 1: 
        print(y, x, z, w)