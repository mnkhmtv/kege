s = open('/home/diana/ЕГЭ/досрок 1/24_7600.txt').readline()
maxx = 0
k = 1
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'QR' or s[i] + s[i + 1] == 'RQ' \
          or s[i] + s[i + 1] == 'QS' or s[i] + s[i + 1] == 'SQ' \
          or s[i] + s[i + 1] == 'SR' or s[i] + s[i + 1] == 'RS' \
          or s[i] + s[i + 1] == 'QQ' or s[i] + s[i + 1] == 'RR' or s[i] + s[i + 1] == 'SS':
        maxx = max(maxx, k)
        k = 1
        continue
    k += 1
print(maxx)