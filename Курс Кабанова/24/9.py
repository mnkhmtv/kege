s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_1302.txt').readline().replace('XZZY', 'XZZ ZZY').split()
mx = 0
for i in s:
    mx = max(mx, len(i))
print(mx)