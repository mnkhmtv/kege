s = open('/home/diana/ЕГЭ/вариант 25019914/24 (12).txt').readline()
s = 'ABBACCABC'
a = s.split('A')
count = 0
maxx = 0
for i in a:
    if len(i) == 2:
        count += 2
    maxx = max(maxx, count)

    if len(i) < 2 or len(i) > 2: count = 0
    

print(maxx + 2)
