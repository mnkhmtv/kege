count_ = 0
for n in range(800, 901):
    x = n%10
    y = n//10%10
    z = int(str(n)[:1])
    if max(x,y,z) == x:
        max_ = str(x) + str(max(y,z))
    elif max(x,y,z) == y:
        max_ = str(y) + str(max(x,z))
    else:
        max_ = str(z) + str(max(y,x))


    if min(x,y,z) == x and x!=0:
            min_ = str(x) + str(min(y,z))
    elif min(y,z) == y and y!=0:
        min_ = str(y) + str(min(x,z))
    else:
            min_ = str(z) + str(min(y,x))
    
    rasnost = int(max_) - int(min_)
    # print(rasnost)
    

    if rasnost == 30:
        count_+=1
    
print(count_)
