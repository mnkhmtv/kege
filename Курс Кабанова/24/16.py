s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2250.txt').readline().split('A')
mx = 0
for i in range(len(s) - 1):
    mx = max(mx, len(s[i]) + len(s[i+1]) + 1)
print(mx)