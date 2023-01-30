from itertools import product
for x,y,z,w in product(range(2),repeat = 4):
    res = w <= ((x<=z)<=y)

    if res ==0:
        print(x,y,z,w)