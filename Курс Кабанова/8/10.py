from itertools import product

s = 'visna'
k = 0

for i1 in 'vina':
    for i2, i3, i4, i5 in product(s, repeat = 4):
        for i6 in 'vsn':
            if (i1 + i2 + i3 + i4 + i5 + i6).count('v') <= 1:
                k += 1
print(k)