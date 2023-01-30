for i in range(1,30):
    n = bin(i)[2:]
    if n.count('1')%2==0:
        n1 = '10' + n[:-2] + '00'
    else:
        n1 = '11' + n[:-2] + '11'
    r = int(n1,2)
    print(r)