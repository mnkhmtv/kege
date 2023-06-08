s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2420.txt').readline()
s = s.replace('A', '0').replace('B', '0').replace('E', '0').replace('F', '0')
mx = k = 0
for i in range(len(s)):
    if s[i] == '0':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)