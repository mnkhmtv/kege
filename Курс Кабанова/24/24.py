s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_5171.txt').readline()
k = mx = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'CA':
        k = 2   
        for j in range(i + 2, len(s) - 1, 2):
            if s[j] + s[j + 1] == 'CA':
                k += 2
            else:
                if s[j] == 'C':
                    k += 1
                break 
        mx = max(mx, k)
print(mx)