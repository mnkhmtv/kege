# ¬ (y → x) ∨ (z → w) ∨ ¬z,
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                res = not(y <= x) or (z <= w) or not(z)
                if res == 0 :
                    print(x,y,z,w)