from itertools import product
for x,y,z,w in product(range(2), repeat = 4):
    res = ((x<=z)<=y) or (not(w))
    if res == 0:
        print(x,y,z,w)