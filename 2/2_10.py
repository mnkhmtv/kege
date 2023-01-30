#  ((x ∨ ¬y) ∧ (¬z ≡ w)) → (y ∧ z).
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                res = ((x or not(y)) and (not(z) == w)) <= (y and z)
                if res == 0:
                    print(x,y,z,w)