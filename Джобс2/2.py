from itertools import product
for x, y, z in product(range(2), repeat = 3):
    res = (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not(y) and not(z))
    if res == 1:
        print(x,y,z)