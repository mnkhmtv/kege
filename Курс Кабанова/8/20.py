from itertools import product

s = 'aimru'
n = 1
for i1, i2, i3, i4 in product(s, repeat=4):
    if n == 211:
        print(i1 + i2 + i3 + i4)
    n += 1