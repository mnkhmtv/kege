for i in range(1, 1000):
    n = bin(i)[2:]
    s = [k for k in n]
    n1 = []
    for j in s:
        if j == '0':
            n1.append('1')
        else:
            n1. append('0')
    n1 = ''.join(n1)
    n2 = '1' + n1
    if n2.count('1') % 2 == 0:
        n3 = n2 + '0'
    else:
        n3 = n2 +'1'

    res = int(n3, 2)
    if res > 180:
        print(i)
        input()
    
