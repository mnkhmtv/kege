s = '012345678'
s1 = '2468'
s5 = '0234567'
k = 0
for i1 in s1:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s5:
                    res = i1+i2+i3+i4+i5
                    if res.count('3')<= 1:
                        k+=1
print(k)
