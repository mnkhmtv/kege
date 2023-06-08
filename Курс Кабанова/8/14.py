from itertools import product

s = 'deikstra'
k = 0

for i1, i2, i3, i4, i5, i6 in product(s, repeat = 6):
    res = i1 + i2 + i3 + i4 + i5 + i6
    if res.count('i') == 1:
        if res.count('ie') == 0 and res.count('ia') == 0 and i6 != 'i':
            if len(res) == len(set(res)):
                k += 1
print(k)
