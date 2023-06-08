s = open('/home/diana/ЕГЭ/ТТ 2023/24/24_2427.txt').readline()
ans = string = s[0]
for i in range(len(s) - 1):
    if s[i] >= s[i + 1]:
        string += s[i + 1]
        if len(string) > len(ans):
            ans = string
    else:
        string = s[i + 1]
print(ans)
