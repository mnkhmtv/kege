s = open('/home/diana/ЕГЭ/досрок 2/26_7626.txt')
k = int(s.readline())
n = int(s.readline())
all = [list(map(int, i.split())) for i in s]
# print(all[:10])
all.sort()
count = 0
p = 0
hran = [0] * k
# print(hran[:10])
for i in range(n):
    for j in range(k):
        if all[i][0] > hran[j]:
            count += 1
            hran[j] = all[i][1]
            p = j + 1 # нумеруется с 1
            break
print(p, count)