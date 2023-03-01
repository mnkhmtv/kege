s = open('/home/diana/ЕГЭ/Школково-2/27B.txt')
n = int(s.readline())
k = int(s.readline())
all = [int(i) for i in s]
count1 = 0
count2 = 0
for i in range(n):
    count1 += min(n - abs(k - i), abs(k - i)) * all[i]

if k == n:
    k == 0
else:
    k += 1

for i in range(n):
    count2 += min(n - abs(k - i), abs(k - i)) * all[i]
print(abs(count1 - count2))
