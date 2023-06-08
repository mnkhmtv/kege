s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_1146.txt').readline()
s = s.replace('B', 'A').replace('C', 'A').replace('E', 'A').replace('F', 'A').split('A')
mn = 1e9
for i in range(len(s)):
    if len(s[i]) > 1:
        mn = min(mn, len(s[i]))
print(mn)