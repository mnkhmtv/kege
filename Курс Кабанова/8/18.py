from itertools import product

s = 'agilmort'
n = 1
for i1, i2, i3, i4 in product(s, repeat=4):
    if i3 + i4 == 'im':
        print(n)
    n += 1
    