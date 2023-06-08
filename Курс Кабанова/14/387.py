alp16 = '0123456789ABCDEF'
k = ans = 0
for x in alp16:
    k = 0
    res = int('8569' + x, 16) + int('12' + x + '48', 16)
    res8 = ''
    while res > 0:
        if (res % 8) % 2 == 0:
            k += 1
        res8 += str(res % 8)
        res //= 8
    if k <= 2:
        ans = res8
print(ans)

result = ""
for x in alp16:
    n = int('8569' + x, 16) + int('12' + x + '48', 16)
    k = 0
    s = ""
    while n > 0:
        if n % 2 == 0:
            k += 1
        s = str(n % 8) + s
        n //= 8
    if k <= 2:
        result = s
print(result)
