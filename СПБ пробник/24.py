s = open('/home/diana/ЕГЭ/СПБ пробник/24.txt').readline()
print(s[:10])
k = 0
maxx = 0
for i in range(1, len(s) - 1, 2):
    if int(s[i - 1]) % 2 == 0 and int(s[i]) % 2 != 0:
        k += 1
    else:
        maxx = max(maxx, k)
        k = 0
print(maxx)
