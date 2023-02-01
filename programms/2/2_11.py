#  (¬a ∧ ¬b) ∨ (b ≡ c) ∨ d.
from itertools import product

for a,b,c,d in product(range(2),repeat=4):
    s = ((not(a)) and (not(b))) or (b==c) or d
    if s == 0:
        print(a,b,c,d)
