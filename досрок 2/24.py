s = open('/home/diana/ЕГЭ/досрок 2/24_7624.txt').readline()
maxx = k = 1
a = ['XX', 'YY', 'ZZ', 'XY', 'XZ', 'YX', 'YZ', 'ZY', 'ZX']
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) not in a:
        k += 1
    else:
        maxx = max(k, maxx)
        k = 1
print(maxx)
