for i in range(1, 9):
    n = bin(i)[2:]
    if i % 2 == 0:
        n1 = '10' + n
    else:
        n1 = '1' + n + '01'
    
    res = int(n1, 2)
    print(res)