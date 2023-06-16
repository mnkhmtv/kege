s = open('/home/diana/ЕГЭ/dev inf/пробник/26 (10).txt')
k = int(s.readline())
n = int(s.readline())
times = []
for i in range(n):
    times += [[int(i) for i in s.readline().split()]]
opers = []
for i in range(k):
    opers.append(i+1)

