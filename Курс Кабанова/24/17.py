s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2251.txt').readline().split('D')
mx = 0
for i in range(len(s) - 2):
    mx = max(mx, len(s[i]) + len(s[i + 1]) + len(s[i + 2]) + 2)
print(mx)
