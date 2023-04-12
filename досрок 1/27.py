s = open('/home/diana/ЕГЭ/досрок 1/27A_7603.txt')
n = int(s.readline())
k = int(s.readline())
a = [int(i) for i in s]
maxx = 0
for i in range(n - k):
    for j in range(i + k, n):
        maxx = max(maxx, a[i] + a[j])
print(maxx)
