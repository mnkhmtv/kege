s = open('/home/diana/ЕГЭ/открытый досрок/1_17.txt')
a = [int(i) for i in s]
maxx = 0
for i in a:
    if 9 < i < 100:
        maxx = max(maxx, i)

dv = [i for i in range(10, 100)]
count = 0
maxs = 0
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]
    if (a[i] in dv and a[i + 1] not in dv) or (a[i + 1] in dv and a[i] not in dv):
        if summ % maxx == 0:
            count += 1
            maxs = max(summ, maxs)
print(count, maxs)
