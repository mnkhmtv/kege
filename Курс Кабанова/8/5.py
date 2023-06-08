from itertools import product
s = 'salo'
k = 0
for i1, i2, i3, i4, i5, i6 in product(s, repeat = 6):
    res = i1 + i2 + i3 + i4 + i5 + i6
    if 1 <= res.count('o') <= 3:
        k += 1
print(k)