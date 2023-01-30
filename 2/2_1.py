# ((¬x ∨ z) ≡ (y ∧ ¬w)) → (z ∧ y)
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                s = not((not(x) or z) == (y and not(w))) or (z and y)
                if s == False:
                    print(x,y,z,w,s)