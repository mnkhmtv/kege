s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_4643.txt').readline()

s = s.replace('2', '1').replace('B', 'A')
mx = k = 0

for i in range(len(s) - 2):

    if s[i] + s[i + 1] + s[i + 2] == '11A':

        k = 1

        for j in range(i + 3, len(s) - 2, 3):

            if s[j] + s[j + 1] + s[j + 2] == '11A':
                k += 1

            else:
                break

        mx = max(mx, k) 

print(mx)