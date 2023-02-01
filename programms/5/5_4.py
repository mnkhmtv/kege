for _ in range(1,22):
    n = int(str(_) + str(_%10))
    
    bin_ = bin(n)[2:]

    if bin_.count('1') % 2 == 0:
        bin_ = bin_ + '0'
    else:
        bin_ = bin_ + '1'
    
    result = int(bin_, 2)

    if result>413:
        print(_)
        break

