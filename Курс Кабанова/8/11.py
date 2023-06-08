from itertools import product

s = 'abcd'
k = 0

for i1, i2, i3, i4 in product(s, repeat = 4):
    if i1 <= i2 <= i3 <= i4:
        k += 1

print(k)