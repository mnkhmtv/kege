s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_865.txt').readline().replace('F', 'C')
mx = k = 0
for i in range(len(s)):
    if s[i] != 'C':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)