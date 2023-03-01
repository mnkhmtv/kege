for k in range(0, 100):
    if k > 9:
        k1 = k * int(str(k)[0])
    else:
        k1 = k * 0
    
    if k1 > 9:
        k2 = k1 + int(str(k)[-1])
    else:
        k2 = k1 + k1
    
    if k2 == 860: print(k)