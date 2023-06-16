s = open('/home/diana/ЕГЭ/Джобс 02.06/24_8959.txt').readline()

k = mx = 0
for i in range(len(s) - 1):
    if s[i] + s[i+1] == 'EA':
        k = 2
        for j in range(i + 2, len(s) - 1, 2):
            if s[j] + s[j+1] == 'EA':
                k += 2
            else:
                break
    mx = max(mx, k)

mx1 = k1 = 0
for i in range(len(s) - 2):
    if s[i] + s[i+1] + s[i+2] == 'NPC':
        k1 = 3
        for j in range(i + 3, len(s) - 1, 3):
            if s[j] + s[j+1] + s[i+2]== 'NPC':
                k1 += 3
            else:
                break
    mx1 = max(mx1, k1)

mx2 = k2 = 0
s = s.replace('NPC', '3').replace('EA', '2')
for i in range(len(s)):
    if s[i] == '3' or s[i] == '2':
        k2 += int(s[i])
    else:
        mx2 = max(mx2, k2)
        k2 = 0
print(max(mx1, mx2, mx))