s = open('/home/diana/ЕГЭ/Марат Ишимов1/24_5641.txt').readline()
s = s.replace('NP', 'N P')
s = s.replace('PO', 'P O')
a = s.split(' ')
maxx = 0
for i in a:
    maxx = max(len(i), maxx)
print(maxx)