from itertools import product
s = 'avlor'
k = 0

for i1, i2, i3, i4 in product(s, repeat = 4):
    res = i1 + i2 + i3 + i4
    k += 1
    if i1 == 'l':
        print(k)
        break