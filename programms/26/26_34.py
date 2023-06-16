f = open('/home/diana/ЕГЭ/programms/26/26_34.txt') 
n = int(f.readline()) 
a = list(map(int, f.readlines())) 
a.sort(reverse = True) 
tek = a[0] 
k = 1
for i in range(n): 
    if a[i] <= tek - 5: 
        k += 1 
        tek = a[i] 
print(k, tek)
