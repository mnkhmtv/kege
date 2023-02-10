from itertools import product

s = 'abcdx'
count = 0
for i1, i2, i3, i4 in product(s, repeat = 4):
    res = i1 + i2 + i3 + i4
    if res.count('x') == 1:
        count += 1
print(count)