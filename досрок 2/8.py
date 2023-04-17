from itertools import product
s = 'aklmny'
k = 0
for i1, i2, i3, i4, i5 in product(s, repeat = 5):
    res = i1 + i2 + i3 + i4 + i5
    k += 1
    if i1 + i2 == 'km':
        print(k)
        break