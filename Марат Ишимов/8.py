from itertools import product

s = '01234567'
count = 0
for i1 in '246':
    for i2, i3, i4 in product(s, repeat = 3):
        for i5 in '013457':
            res = i1 + i2 + i3 + i4 + i5
            if res.count('7')<= 2:
                count += 1
print(count)

