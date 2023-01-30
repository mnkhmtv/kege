a = [str(i) for i in range(1000)]
a.append('')
print('a')
s = '0123456789'
need = []
for i1 in a:
    for i2 in s:
        delit = []
        res = int('3' + str(i1) + '52' + i2)
        if res/int(res**0.5)==res**0.5:
            for i in range(2,int(res**0.5)+1):
                if res%i==0:
                    delit+=[res//i]
            need+=[[res,max(delit)]]
need.sort()
print(need)

