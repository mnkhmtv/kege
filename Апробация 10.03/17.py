s = open('/home/diana/ЕГЭ/Апробация 10.03/17.txt')
a=  [int(i) for i in s]
k = 0 
for i in a:
    if i % 3 == 0:
        k += 1

maxx = -1e9
count = 0
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]
    if (a[i] < 0 or a[i + 1] < 0) and summ < k:
        count += 1
        maxx = max(maxx, summ)
print(count, maxx)