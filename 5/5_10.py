
for i in range(1,10000):
    n = bin(i)[2:]

    n1 = n + str(n.count('1')%2)
    n2 = n1 + str(n1.count('1')%2)

    res = int(n2,2)
    
    if res>77:
        print(i)
        break