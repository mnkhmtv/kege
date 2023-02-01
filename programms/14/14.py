# yAAx 12 + x02y 14
ss = '0123456789AB'
res = []
for x in ss:
    for y in ss:
        ss_12 = int(y + 'AA' + x, 12) + int(x + '02' + y, 14)
        # ss_14 = int(x + '02' + y, 14)
        # summ = ss_12 + ss_14
        if ss_12%80 == 0:
            res+=[ss_12]
print(min(res)//80)