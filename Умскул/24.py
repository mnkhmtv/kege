s = open('/home/diana/ЕГЭ/пробник 09.2022/24 (5).txt')
s = s.readline()
k = 0
s = s.replace('A','B')
s = s.replace('1','2')
s = s.replace('22B','!')
s = s.replace('B',' ')
s = s.replace('2', ' ')
maxx = 0
s = s.split()
for i in s:
    maxx = max(maxx,len(i))
print(maxx)