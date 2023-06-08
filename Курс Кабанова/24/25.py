s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2425.txt').readline()
mx = k = 0

for i in range(len(s) - 3):
    if s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'DBAC':
        k = 4
        for j in range(i + 4, len(s) - 3, 4):
            if s[j] + s[j + 1] + s[j + 2] + s[j + 3] == 'DBAC':
                k += 4
            else:
                if s[j] + s[j + 1]  + s[j + 2] == 'DBA':
                    k += 3
                elif s[j] + s[j + 1]  == 'DB':
                    k += 2
                elif s[j] == 'D':
                    k += 1
                break
        mx = max(mx, k)
print(mx)