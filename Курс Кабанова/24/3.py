s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2421.txt').readline()
mx = k = 0
for i in range(len(s)):
    if s[i] != 'D':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)