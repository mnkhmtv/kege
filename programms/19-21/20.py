def f(x,y,p):
    if p == 3 and x+y>=93:
        return True
    elif p == 3 and x+y<93:
        return False
    elif x+y>=93:
        return False
    
    
    if p%2==0: return f(x+1,y,p+1) or f(x*2,y,p+1) or f(x,y+1,p+1) or f(x,y*2,p+1)
    else: return f(x+1,y,p+1) and f(x*2,y,p+1) and f(x,y+1,p+1) and f(x,y*2,p+1)

for s in range(1,81):
    if f(12,s,0)==1:
        print(s)
        
        