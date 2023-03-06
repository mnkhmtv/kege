for i in range(1, 1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n1 = '1' + n[:-2] + '10'
    else:
        n1 = '10' + n[2:] + '1'

    res = int(n1, 2)
    if res > 202:
        print(i)
        input(

            
        )