from itertools import product

s = 'ab123'
k = 0
for i1, i2, i3, i4, i5, i6, i7, i8 in product(s, repeat = 8):
    res = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
    if res.count('a') + res.count('b') == 2:
        k += 1
print(k)