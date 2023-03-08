s = open('/home/diana/ЕГЭ/03.03.2023/17pr.txt')
a = [int(i) for i in s]

count = 0
maxs = -1e9
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]
    if (a[i] % 2 == 0 and a[i + 1] < 0) or (a[i] < 0 and a[i + 1] % 2 == 0):
        count += 1
        maxs = max(maxs, summ)
print(count, maxs)