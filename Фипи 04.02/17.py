s = open('/home/diana/ЕГЭ/вариант 25019914/17 (16).txt')
a = [int(i) for i in s]
s = open('/home/diana/ЕГЭ/вариант 25019914/17 (16).txt')
k = [int(i) for i in s]
k.sort(reverse = 1)
max_a = 0
for i in k:
    if i % 10 == 9:
        max_a = i ** 2
        break

count = 0
minn = 10 ** 20
for i in range(len(a) - 1):
    summ = a[i] ** 2 + a[i + 1] ** 2
    if (a[i] % 10 == 9 or a[i + 1] % 10 == 9) and summ < max_a:
        count += 1
        minn = min(minn, summ)

print(count, minn)