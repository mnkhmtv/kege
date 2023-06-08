s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_1145.txt').readline().split('D')
mn = 1e9
for i in range(len(s)):
    if len(s[i]) > 2:
        mn = min(len(s[i]) + 2, mn)
print(mn)


