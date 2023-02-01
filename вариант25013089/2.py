from itertools import product

for a, b, c in product(range(2), repeat = 3):
    
    res = (a and not(c)) or (not(b) and not(c))
    print(a, b, c, res)