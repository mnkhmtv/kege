s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2422.txt').readline()
mx = k = 0
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        k += 1
    else:
        k += 1
        mx = max(mx, k)
        k = 0
print(mx)