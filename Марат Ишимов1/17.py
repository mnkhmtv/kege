s = open('/home/diana/ЕГЭ/Марат Ишимов1/17_5635.txt')
a = [int(i) for i in s]
maxx = -1e9
minn = 1e9
for i in a:
    if str(abs(i))[-2:] == '31':
        minn = min(minn, i)
        maxx = max(maxx, i)
abss = abs(minn + maxx)

k = 0
mx = -1e9
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]
    if a[i] > abss and a[i + 1] > abss:
        k += 1
        maxx = max(maxx, summ)
print(k, maxx)