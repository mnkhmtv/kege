s = open('/home/diana/ЕГЭ/Марат Ишимов/24_5641.txt').readline()
s = s.replace('NP', 'N P')
s = s.replace('PO', 'P O')
a = s.split()
maxx = 0
for i in a:
    maxx = max(maxx, len(i))
print(maxx)
