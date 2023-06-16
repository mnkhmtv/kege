def f(a, b, c):    
     if (a*b) > c:
        return 1    
     else:
        return 0
for a in range(-100, 100):    
    flag = 1
    for x in range(1, 250):        
        for y in range(1, 250):
            flag*= ((not(f(x, y, a + 13))) <= f(28, y, 520) or f(x, 25, 800))
            if flag == 0:
                break
    if flag:        
        print(a)
        