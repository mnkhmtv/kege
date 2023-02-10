s = open('/home/diana/ЕГЭ/вариант 25013090/17 (15).txt')
a = [int(i) for i in s]

max_a = -1e9
for i in a:
    if i % 11 == 0:
        max_a = max(max_a, i)

count = 0
maxx = -1e9
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]

    if (a[i] % 11 == 0 or a[i + 1] % 11 == 0) and summ <= max_a:
        count += 1
        maxx = max(maxx, summ)

print(count, maxx)