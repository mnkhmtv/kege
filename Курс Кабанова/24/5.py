s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2426.txt').readline().replace('2', '1').replace('3', '1')
mx = k = 0
for i in range(len(s)):
    if s[i] == '1':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
print(mx)