s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_66.txt').readline().replace('KOT', '1')
mx = k = 0
for i in range(len(s)):
    if s[i] == '1':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)
