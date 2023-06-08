s = open('/home/diana/ЕГЭ/пробник 09.2022/17 (6).txt')
a = [int(i) for i in s]
k = 0
ost = min(a)
maxx = 0
for i in range(len(a)-1):
    if a[i]%117==ost or a[i+1]%117==ost:
        summ = a[i] + a[i+1]
        k+=1
        maxx = max(maxx,summ)

print(k,maxx)