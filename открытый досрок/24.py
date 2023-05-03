s = open('/home/diana/ЕГЭ/открытый досрок/1_24.txt').readline()
maxx = k = 1
a = ['AB', 'AC', 'BA', 'CA', 'BC', 'CB', 'AA', 'BB', 'CC']
for i in range(len(s) - 1):
    x = s[i] + s[i + 1] 
    if x in a:
        maxx = max(maxx, k)
        k = 1
    else:
        k += 1
        maxx = max(maxx, k)
print(maxx)
