s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_4602.txt').readline()
s = s.replace('C', 'B').replace('D', 'B').replace('O', 'A').replace('BA', '*')
k = mx = 0
for i in range(len(s)):
    if s[i] == '*':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)
