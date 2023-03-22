s = open('/home/diana/ЕГЭ/10 вариант/17.txt')
a = [int(i) for i in s]
count = 0
minn = 1e9
for i in range(len(a) - 1):
    rasn = abs(a[i] - a[i + 1])
    if abs(a[i]) % 10 == 7 and abs(a[i + 1]) % 10 == 7:
        count += 1
        minn = min(minn, rasn)
print(count, minn)    