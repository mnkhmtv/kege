from itertools import product

s = 'elmry'
n = 1

for i1, i2, i3, i4 in product(s, repeat=4):
    if i1 == 'l':
        print(n)
        break
    n += 1
