from itertools import product

s = 'mikra'
k = 0
for i1, i2, i3, i4, i5, i6, i7, i8 in product(s, repeat = 8):
    res = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
    if res.count('m') == 2 and res.count('i') == 3 and res.count('k') == 1 and \
    res.count('r') == 1 and res.count('a') == 1:
        k += 1
print(k)