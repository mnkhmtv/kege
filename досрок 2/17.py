s = open('/home/diana/ЕГЭ/досрок 2/17_7619.txt')
a = [int(i) for i in s]
maxx = 0
for i in a:
    if 9 < i < 100:
        maxx = max(maxx, i)
maxs = k = 0
dv = [i for i in range(10, 100)]
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]
    if ((a[i] in dv and a[i + 1] not in dv) or \
          (a[i + 1] in dv and a[i] not in dv)) and summ % maxx == 0:
        k += 1
        maxs = max(maxs, summ)
print(k, maxs)
