for i1 in 0,1:
    for i2 in 0,1:
        for i3 in 0,1:
            for i4 in 0,1:
                res = (i3 <= i1) <= (i4 or not(i2))
                if res == 0:
                    print(i1, i2, i3, i4)