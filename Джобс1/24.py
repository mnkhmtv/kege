s = open('/home/diana/ЕГЭ/вариант25013089/24 (9).txt').readline()

non = 'GWP'
maxx = 0
count = 0
for i in s:
    if i not in non:
        count += 1
        maxx = max(count, maxx)
    else:
        count = 0

print(maxx)