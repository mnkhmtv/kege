s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_1428.txt').readline().replace('XY','X Y').replace('XZ', 'X Z').split()
mx = 0
for i in s:
    mx = max(mx, len(i))
print(mx)

