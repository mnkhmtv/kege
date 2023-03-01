s = 40 * '123'
while '12' in s or '333' in s:
    if '12' in s:
        s = s.replace('12', '3', 1)
    else:
        s = s.replace('333', '3', 1)


print(s)