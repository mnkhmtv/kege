s = open('/home/diana/ЕГЭ/Джобс 02.06/26_8961.txt')
k, m, n = map(int, s.readline().split())
print(k, m, n)
arr = [int(i) for i in s]
print(arr[:10])
arr.sort(reverse=True)
ost = [m] * k
ver = 0
for i in arr:
    for j in range(k):
        if ost[j] >= i:
            ost[j] -= i
            ver += 1
            break
print(ver, sum(ost))
