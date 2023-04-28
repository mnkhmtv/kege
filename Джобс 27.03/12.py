s = 38 * '1'
s1 = 34 * '2'
s2 = 30 * '3'
maxx = 0
for i in range(39):
    for j in range(35):
        for k in range(31):
            s = j * '2' + i*'1' +(38 - i) * '1' +(30 - k) * '3' + k*'3'+ (34 - j) *'2'
            while '33' in s or '11' in s or '22' in s:
                if '33' in s:
                    s = s.replace('33', '12', 1)
                if '11' in s:
                    s = s.replace('11', '32', 1)
                if '22' in s:
                    s = s.replace('22', '31', 1)
            maxx = max(sum(map(int, s)), maxx)
print(maxx)