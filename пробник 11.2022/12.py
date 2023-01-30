count = 0
for n in range(1,101):
    s = '1' + n*'0'
    while '10' in s or '1' in s:

        if '10' in s:
            s = s.replace('10', '0001', 1)

        elif '1' in s:
            s = s.replace('1', '0', 1)

    if len(s)%7==0:
        count+=1

print(count)

