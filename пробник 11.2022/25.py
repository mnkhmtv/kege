a = [str(i) for i in range(1000)]
a.append('')
print('a')
s = '0123456789'
need = []
for i1 in a:
    for i2 in s:
        delit = []
        res = int('3' + str(i1) + '52' + i2)

        for i in range(2,int(res**0.5)+1):
            if res%i==0:
                delit+=[i]
                delit.sort()

        if len(set(delit))%2!=0:
            need+=[[res, max(delit)]]
            
print(need)