# (¬x ≡ z) → (y ≡ (w ∨ x)).
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                res = (not(x)==z) <= (y==(w or x))
                if res == 0:
                    print(x,y,z,w)