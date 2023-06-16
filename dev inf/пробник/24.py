s = open('/home/diana/ЕГЭ/dev inf/пробник/24 (17).txt').readline()
# s = 'AAADDDFEDFEDFQWERTTGT6FVFS'
mx = k = 1

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        k += 1
    else:
        mx = max(mx, k)
        k = 1
print(mx)