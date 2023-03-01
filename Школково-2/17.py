s = open('/home/diana/ЕГЭ/Школково-2/17.txt')
a = [int(i) for i in s]

maxx = 0
count = 0
for i in range(len(a) - 2):
    summ = a[i] + a[i + 1] + a[i + 2]
    sr = summ / 3
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0 or a[i + 2] % 3 == 0) and summ % 2 == 0 and a[i + 1] > sr:
        count += 1
        maxx = max(summ, maxx)
print(count, maxx)
