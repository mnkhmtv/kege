#  (x ∨ ¬y) ∧ ¬(w ≡ z) ∧ w.
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                res = (x or not(y)) and not(w==z) and w
                if res == 1:
                    print(x,y,z,w)