a = ['']
for i in range(0, 100000):
    a.append(str(i))
need = []

for i in a:
    for j in a:
        res = int('8' + i + '80' + j + '06')
        if res < 10**10:
            if res % 4546 == 0:
                print(res, res // 4546)
        
need.sort()
print(len(need))