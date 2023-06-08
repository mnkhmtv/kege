from itertools import product

s = 'vaify'
k = 0

for i1 in 'vafy':
    for i2, i3, i4 in product(s, repeat = 3):
        res = i1 + i2 + i3 + i4
        if len(res) == len(set(res)):
            if res.count('vf') == 0 and res.count('fv') == 0:
                k += 1
print(k)