for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                res = ((not(x) and y )==z) and w
                if res == 1:
                    print(x,y,z,w)