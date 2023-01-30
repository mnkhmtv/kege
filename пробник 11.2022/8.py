from itertools import product

s = 'арбуз'
count = 0

for i1, i2, i3, i4, i5, i6 in product(s, repeat = 6):
    res = i1 + i2 + i3 + i4 + i5 + i6
    if res.count('а') == 3 and res.count('аа')==1 and res.count('ааа')==0:
        count+=1

print(count)