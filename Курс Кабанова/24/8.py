s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_1975.txt').readline().replace('PP', 'P P').split()
mx = 0
for i in s:
    mx = max(mx, len(i))
print(mx)