for n in range(1,1000):
    bin_ = bin(n)[2:]

    if bin_.count('1') > bin_.count('0'):
        bin_ = bin_ + '0'
    else:
        bin_ = '11' + bin_
    
     
    if bin_.count('1') > bin_.count('0'):
        bin_ = bin_ + '0'
    else:
        bin_ = '11' + bin_
        
    result = int(bin_, 2)
    
    if result>500:
        print(n)
        break