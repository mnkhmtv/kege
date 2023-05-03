from itertools import product
print('x y z w')
for x, y, z, w in product(range(2), repeat = 4):
    res = (x or (not(y))) and (not(y == z)) and (not(w))
    if res == 1:
        print(x, y, z, w)