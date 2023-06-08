from itertools import product

s = 'gepard'
k = 0

for i1 in 'geprd':
    for i2, i3, i4 in product(s, repeat = 3):
        for i5 in 'gpard':
            if (i1 + i2 + i3 + i4 + i5).count('g') == 1:
                k += 1
print(k)