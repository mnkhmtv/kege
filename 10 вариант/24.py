s = open('/home/diana/ЕГЭ/10 вариант/24.txt').readline()
maxx = 0
k = 0
pred = s[0]
for i in range(1, len(s)):
    if pred >= s[i]:
        k += 1
    else:
        maxx = max(maxx, k)
        k = 0
    pred = s[i]

print(maxx)
    