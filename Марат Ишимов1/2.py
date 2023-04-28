from itertools import product
print('x y z w')
for x, y, z, w in product(range(2), repeat = 4):
    res = (not(z <= x)) or (y == w) or w
    if res == 0:
        print(x, y, z, w)