k = 0
s = 'декор'
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                res = i1+i2+i3+i4
                k+=1
                if res[0]=='к':
                    print(k)
                    break
                