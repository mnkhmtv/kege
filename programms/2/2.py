print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = not(not(y) or x) or (not(z) or w) or not(z)
                if not(F):
                    print(x,y,z,w)