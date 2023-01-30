a = ['']
for i in range(0,100):
    a.append(str(i))

need = []
for i in a:
    res = '123' + i + '890'
    if int(res)%27==0:
        need+=[[res,int(res)//27]]

need.sort()

for i in need:
    print(i)