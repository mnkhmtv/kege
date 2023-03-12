s = '0123456'
count = 0
for i1 in '123456':
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    res = i1 + i2 +  i3 + i4 + i5
                    k_ch = res.count('2')*2 + res.count('4')*4 + res.count('6')*6
                    k_nch = res.count('1')*1 + res.count('3')*3 + res.count('5')*5
                    
                    if res.count('6') == 1:
                        if k_nch > k_ch:
                            count += 1
print(count)
