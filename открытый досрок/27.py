s = open('/home/diana/ЕГЭ/открытый досрок/1_27_B.txt')
k = int(s.readline())
n = int(s.readline())
print(k, n)
a = [int(i) for i in s]
maxx = 0
count = 0
for i in range(n - k):
    for j in range(i + k, n):
        maxx = max(a[i] + a[j], maxx)
        print(maxx)


print(maxx)