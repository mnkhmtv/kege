from itertools import product
s = 'АЙКОС'
k = 0
for i1, i2, i3, i4, i5 in product(s, repeat = 5):
    res = i1 + i2 + i3 + i4 + i5
    k += 1
    if res.count('О') <= 1 and res.count('СС') == 0 and res.count('ССС') == 0 \
        and res. count('СССС') == 0 and res.count('ССССС') == 0:
        print(k)