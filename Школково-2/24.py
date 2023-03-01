s = open('/home/diana/ЕГЭ/Школково-2/24.txt').readline()

s = s.replace('DD', '1')
s = s.replace('VV', '2')
s = s.replace('MM', '3')

ss = ''
need = []
for i in range(len(s)):
    if s[i] == '1' or s[i] == '2' or s[i] == '3':
        ss += s[i]
    else:
        need += [ss]
        ss = ''

maxx = 0
for i in need:
    if i.count('1') > 0 and i.count('2') == 0 and i.count('3') == 0:
        continue
    elif i.count('1') == 0 and i.count('2') > 0 and i.count('3') == 0:
        continue
    elif i.count('1') == 0 and i.count('2') == 0 and i.count('3') > 0:
        continue
    else:
        maxx = max(len(i) * 2, maxx)
print(maxx)