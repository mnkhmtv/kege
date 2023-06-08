a = ['AA', 'BB', 'CC', 'AB' 'AC', 'BA', 'BC', 'CA', 'CB']
s = open('/home/diana/ЕГЭ/16.05/24 (16).txt').readline()
k = 1
maxx = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1]  in a:
        maxx = max(maxx, k)
        k += 1
    else:
        k = 1
print(k)