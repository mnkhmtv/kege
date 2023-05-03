from itertools import product
k = 0
for i1, i2, i3, i4 in product('abzi', repeat = 4):
    k += 1
    if i1 + i2 + i3 + i4 == 'izba':
        print(k)