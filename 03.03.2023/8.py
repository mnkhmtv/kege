from itertools import product
s = '0123456'
count = 0
for i1 in '123456':
    for i2, i3, i4, i5, i6 in product(s, repeat = 5):
        res = i1 + i2 + i3 + i4 + i5 + i6
        if res.count('5') == 1:
            if res.count('14') == 0 and res.count('41') == 0 \
            and res.count('34') == 0 and res.count('43') == 0 \
            and res.count('54') == 0 and res.count('45') == 0:
                if int(res, 7) % 14 == 0:
                    count += 1
print(count)