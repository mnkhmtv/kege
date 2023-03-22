s = '01234'
need = []
for i1 in '1234':
    for i2 in s:
        for i3 in s:
            res = int(i1 + i2 + i3)
            if int(i3) < int(i2)  < int(i1):
                need += [res]
print(len(set(need)))