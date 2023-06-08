from itertools import product
s = 'lodka'
k = 0
for i1, i2, i3, i4 in product(s, repeat = 4):
    res = i1 + i2 + i3 + i4
    if res.count('o') >= 2:
        k += 1
print(k)