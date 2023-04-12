s = open('/home/diana/ЕГЭ/досрок 1/17_7596.txt')
a = [int(i) for i in s]

mina = 1e9
for i in a:
    if i % 10 == 5 and 99 < i < 1000:
        mina = min(mina, i)

count = 0
minn = 1e9
for i in range(len(a) - 1):
    summ = a[i] + a[i + 1]
    if (99 < a[i] < 1000 and (a[i + 1] < 100 or a[i + 1]  >= 1000)) or (99 < a[i + 1] < 1000 and (a[i] < 100 or a[i]  >= 1000)):
        if summ % mina == 0:
            count += 1
            minn = min(minn, summ)
print(count, minn)