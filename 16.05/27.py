s = open('/home/diana/ЕГЭ/16.05/27_A.txt')
k = int(s.readline())
n = int(s.readline())
a = [int(i) for i in s]
mx = -1e9
for i in range(n):
    for j in range(1, n):
        summ = a[i] + a[j]
        rsn = abs(a[i] - a[j])
        if (j - k) >= k and rsn % 2 != 0 and (a[i] % 26 == 0 or a[j] % 2 == 0):
            mx = max(mx, summ)
print(mx)