s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_4642.txt').readline().replace('B', 'A').replace('2', '1').replace('A1', '*')
k = mx = 0
for i in range(len(s)):
    if s[i] == '*':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)
