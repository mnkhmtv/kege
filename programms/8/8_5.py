s = 'катер'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            res = i1+i2+i3
            if res.count('р') == 2:
                k+=1
print(k)