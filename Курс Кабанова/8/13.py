from itertools import product

s = '0123456789'
k = 0

for i1 in '123456789':
    for i2, i3 in product(s, repeat = 2):
        if i1 <= i2 <= i3:
            k += 1
print(k)