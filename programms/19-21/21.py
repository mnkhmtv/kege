def f(x,p):
    if (p==2 or p==4) and x>=64:
        return True
    elif p==4 and x<64:
        return False
    elif x>=64:
        return False
    
    if p%2!=0: return f(x+1,p+1) or f(x*3,p+1)
    else: return f(x+1,p+1) and f(x*3,p+1)
    

for s in range(1,63):
    if f(s,0)==1:
        print(s)
print('-----')
def f1(x,p):
    if p==2 and x>=64:
        return True
    elif p==2 and x<64:
        return False
    elif x>=64:
        return False
    
    if p%2!=0: return f1(x+1,p+1) or f1(x*3,p+1)
    else: return f1(x+1,p+1) and f1(x*3,p+1)
    

for s in range(1,63):
    if f1(s,0)==1:
        print(s)