s = open('/home/diana/ЕГЭ/вариант25013089/27-B (1).txt')
n = int(s.readline())

count = 0
mins = {
    'chet' : 0,
    'nechet' : 0
}
ch_nch = [0, 0]
summ = 0
for i in range(n):
    x = int(s.readline())

    if x % 2 == 0 and x > mins['nechet']:
        count += ch_nch[1]

    elif x % 2 != 0 and x > mins['chet']:
        count += ch_nch[0]
    
    if x % 2 != 0:
        ch_nch[1] += 1

        if mins['nechet'] == 0:
            mins['nechet'] = x

        elif x < mins['nechet']:
            mins['nechet'] = x

    elif x % 2 == 0:
        ch_nch[0] += 1

        if mins['chet'] == 0:
            mins['chet'] == x

        elif x < mins['chet']:
            mins['chet'] = x
    

print(count)
