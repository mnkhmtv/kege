from itertools import product
s = 'igrok'
k = 0
for i1 in 'igro':
    for i2, i3, i4, i5 in product(s, repeat = 4):
        res = i1 + i2 + i3 + i4 + i5
        if 'rok' not in res and res.count('i') == 1 and res.count('g') == 1 \
        and res.count('r') == 1 and res.count('o') == 1 and res.count('k') == 1:
            k += 1
print(k)