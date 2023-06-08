s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_1040.txt').readline()
mx = k = 0
for i in range(len(s)):
    if s[i].isdigit():
        k += 1
        continue
    mx = max(mx, k)
    k = 0
print(mx)