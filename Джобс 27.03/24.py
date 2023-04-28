s = open('/home/diana/ЕГЭ/Джобс 27.03/24_7016.txt').readline()
need = []
print(len(s))
m = ''
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] == 'A':
            if s[j] != 'D':
                m += s[j]
            else:
                need += ['A' + m + 'D']
                m = ''
                continue
maxx = 0
for i in need:
    maxx = max(maxx, len(i))
print(maxx)