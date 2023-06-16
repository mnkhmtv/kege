for i in range(1, 300):
    n = bin(i)[2:]
    if i % 2 == 0:
        n1 = n.replace('0', '00').replace('1', '11')
    else:
        n1 = n.replace('0', '2').replace('1', '00').replace('2', '11')
    res = int(n1, 2)
    if res > 60:
        print(i)
        break