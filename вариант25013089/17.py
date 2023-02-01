s = open('/home/diana/ЕГЭ/вариант25013089/17 (13).txt')

a = [int(i) for i in s]

count = 0
maxx = -10**9
for i in range(len(a) - 1):


    summ = a[i] + a[i + 1]
    pr = a[i] * a[i + 1]

    if summ >= 100 and pr < 0:
        count += 1
        maxx = max(maxx, pr)

print(count, maxx)