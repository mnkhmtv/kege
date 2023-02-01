# ¬ (x → w) ∨ (y ≡ z) ∨ y,


for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                s = not(not(x) or w) or (y == z) or y
                if s == 0:
                    print(x,y,z,w,s)
