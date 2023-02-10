from itertools import product
for x, y, z, w in product(range(2), repeat = 4):
    res = not((w or not(y)) and x) or (y == z)
    if res == 0:
        print(x, y, z, w)