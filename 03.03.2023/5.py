for i in range(101, 500):
    n = bin(i)[2:]
    k0 = n.count('0')
    k1 = n.count('1')
    if k0 == k1:
        n1 = n + n[-1]
    elif k0 < k1:
        n1 = n + '0'
    elif k1 < k0:
        n1 = n + '1'
    
    k0 = n1.count('0')
    k1 = n1.count('1')
    if k0 == k1:
        n2 = n1 + n1[-1]
    elif k0 < k1:
        n2 = n1 + '0'
    elif k1 < k0:
        n2 = n1 + '1'
    
    k0 = n2.count('0')
    k1 = n2.count('1')
    if k0 == k1:
        n3 = n2 + n2[-1]
    elif k0 < k1:
        n3 = n2 + '0'
    elif k1 < k0:
        n3 = n2 + '1'
    
    res = int(n3, 2)
    if res % 8 == 0 and res % 16 != 0:
        print(i)
        input()