from itertools import product
k = 0
for i1 in 'WXYZ':
    for i2, i3, i4, i5 in product('ABC', repeat = 4):
        for i6 in 'WXYZ':
            k += 1
print(k)