f = open('/home/diana/ЕГЭ/programms/26/26_35.txt') 
n = int(f.readline()) 
a = [int(x) for x in f.readlines()] 
a.sort() 
res1 = sum(a[:n - n // 5]) 
res2 = sum(a[n // 5: ]) 
print(res1, res2)
