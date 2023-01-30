for n in range(1,128):
    bin_ = bin(n)[2:]

    while len(bin_)<8:
        bin_ = '0'+bin_
    # print(bin_)

    bin_ = bin_.replace('1', '2')
    bin_ = bin_.replace('0', '1')
    bin_ = bin_.replace('2', '0')
    # print(bin_)

    result = int(bin_, 2) + 1
    # print(result)

    if result == 221:
        print(n)

            
