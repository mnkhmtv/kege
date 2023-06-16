f = open('/home/diana/ЕГЭ/programms/26/26_36.txt') 
n = int(f.readline()) 
a = [int(x) for x in f]
a.sort(reverse=True)

res1 = 0 
k = 0 
while len(a) > 0: 
    res = [a[0]] 
    nepodh = [] 
    for i in range(1, len(a)): 
        if res[-1] - a[i] >= 7: 
            res += [a[i] ]
        else: 
            nepodh.append(a[i]) 
    print('res = ', res) 
    print('nepodh =', nepodh) 
    a = [] 
    a += nepodh 
    res1 = max(len(res), res1) 
    k += 1 
    
print(res1, k)
