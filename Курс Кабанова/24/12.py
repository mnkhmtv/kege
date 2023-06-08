s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2423.txt').readline()
mx = k = 0
for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        k += 1
        continue
    k += 1
    mx = max(mx, k)
    k = 0
print(mx)
