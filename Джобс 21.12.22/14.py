a = []
for i in range(0,100):
    if str(i).count('8') == 0 and str(i).count('9') == 0:
        a.append(i)
minn = 1e9
for x in a:
    for y in a:
        s = int('36' + str(x) + '53', 8) - int('4' + str(y) + '3', 8)
        if s > 0:
            minn = min(minn, s)
print(minn)