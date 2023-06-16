from itertools import product
s = 'proliv'
k = 0
for i1, i2, i3, i4, i5, i6 in product(s, repeat=6):
    res = i1 + i2 + i3 + i4 + i5 + i6
    if res.count('p') >= 1:
        k += 1
print(k)