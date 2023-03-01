s = open('/home/diana/ЕГЭ/Джобс 21.12.22/17 (17).txt')

a = [int(i) for i in s]
need = []
n = 0
count = 0
sr = (max(a) + min(a))//2

for i in range(len(a)):
    if n <= 4172:
        need += [[a[i], a[-1-n]]]
        n += 1
    else:
        break
maxx = 0
for i in need:
    summ = i[0] + i[1]
    if (i[0] < sr and i[1] > sr) or (i[1] < sr and i[0] > sr):
        count += 1 
        maxx = max(maxx, summ)

print(count, maxx)