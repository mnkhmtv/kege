s = open('/home/diana/ЕГЭ/Апробация 10.03/24.txt').readline()
k = 0
km = 0
for i in range(0, len(s) - 2, 3):
    if s[i] + s[i + 1] + s[i + 2] == 'CFE' or s[i] + s[i + 1] + s[i + 2] == 'FCE':
        k += 1
    else:
        km = max(km, k)
        k = 0
print(km)