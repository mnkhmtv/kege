s = open('/home/diana/ЕГЭ/пробник 11.2022/24 (6).txt').readline()

splited = s.split('DD')

maxx = 0
count = 0
for i in splited:
    if i.count('FE') >=1:
        count = len(i) + 2
        maxx = max(count, maxx)

print(maxx)