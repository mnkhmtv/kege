s = open('/home/diana/ЕГЭ/Джобс 27.03/17_7020.txt')
a = [int(i) for i in s]
mina = 100
mins = 1e9
k = 0
for i in range(len(a) - 3):
    summ = a[i] + a[i + 1] + a[i + 2] + a[i + 3]
    if abs(a[i]) % 111 != mina and abs(a[i + 1]) % 111 != mina and \
        abs(a[i + 2]) % 111 != mina and abs(a[i + 3]) % 111 != mina:
        k += 1
        mins = min(mins, summ)
print(k, mins)