#  (¬a ∧ ¬b) ∨ (b ≡ c) ∨ d.
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                res = (not(a) and not(b)) or (b==c) or d
                    # print(a,b,c,d)
                if res == 0:
                    print(a,b,c,d)
                    # print(x,y,z,w)