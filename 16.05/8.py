from itertools import product
k = 1
for i1, i2, i3, i4 in product('iklnor', repeat = 4):
    res = i1 + i2 + i3 + i4
    if res == 'kino':
        print(k)
        break
    k += 1