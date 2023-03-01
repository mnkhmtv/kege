from itertools import product

s1 = 'лт'
s2 = 'лето'

count = 0
for i1 in s1:
    for i2, i3, i4 in product(s2, repeat = 3):
        res = i1 + i2 + i3 + i4
        count += 1

print(count)