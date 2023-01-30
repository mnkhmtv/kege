count = 0
c = []
for x in range(1,1000):
    pr = 0
    for a in range(1,1000):
        res = (160<=x<=180)==1 <= (x%35==0 <= x%a==0)
        if res == 1:
            c+=[a]
c = set(c)

        
print(len(c))