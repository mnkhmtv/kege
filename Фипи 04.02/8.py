from itertools import product
s = '0123456'
s1 = '123456'
chet = '0246'
nechet = '135'
count = 0
for i1 in s1:
    for i2, i3, i4, i5, i6 in product(s, repeat = 5):
        res = i1 + i2 + i3 + i4 + i5 + i6
        if res.count('6') == 1:
            if (i1 in chet and i2 in nechet and i3 in chet and i4 in nechet and i5 in chet and i6 in nechet) or (i1 in nechet and i2 in chet and i3 in nechet and i4 in chet and i5 in nechet and i6 in chet):
                count += 1
print(count)