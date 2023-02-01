for n in range(1, 1000):
    s = bin(n)[2:]
    c = s.count('1')
    k = c%2
    s = s + str(k)
    d = s.count('1')
    f = d%2
    s = s + str(f)
    if int(s, 2)>80:
        print(int(s, 2))
        break