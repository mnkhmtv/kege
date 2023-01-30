# (x ≡ ¬y) → (z ≡ (y ∨ w)).
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                res = (not(x==(not(y)))or (z==(y or w)))
                if res == 0:
                    print(x, y, z, w)