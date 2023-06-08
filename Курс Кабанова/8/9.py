from itertools import product

s = '01234'
k = 0
for i1 in '234':
    for i2, i3, i4, i5 in product(s, repeat = 4):
        for i6 in '012':
            k += 1
print(k)