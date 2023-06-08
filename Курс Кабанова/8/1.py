from itertools import product
s = 'kreslo'
k = 0
for i1 in 'krsl':
    for i2, i3 in product(s, repeat = 2):
        for i4 in 'eo':
            k += 1
print(k)
