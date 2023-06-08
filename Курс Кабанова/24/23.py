s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_4546.txt').readline()
k = mx = 0
symb = ['AAA', 'CCC', 'ACA', 'ABA', 'CAC', 'CBC']
for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] in symb:
        k = 1
        for j in range(i + 3, len(s) - 2, 3):
            if s[j] + s[j + 1] + s[j + 2] in symb:
                k += 1
            else:
                break
        mx = max(mx, k)
print(mx)
