#+1 *3 >=66 1<=s<=65

def f(s,p):
    if s>=66 and (p == 2 or p == 4):
        return 1
    elif s>= 66 and p<4:
        return 0
    elif s<66 and p == 4:
        return 0

    if p%2!=0:
        return f(s+1,p+1) or f(s*3,p+1)
    else: 
        return f(s+1,p+1) and f(s*3,p+1)
        
for s in range(1,66):
    if f(s,0):
        print(s)

print('---')

def f1(s,p):
    if s>=66 and p==2:
        return 1
    elif s>= 66 and p<2:
        return 0
    elif s<66 and p == 2:
        return 0

    if p%2!=0:
        return f1(s+1,p+1) or f1(s*3,p+1)
    else: 
        return f1(s+1,p+1) and f1(s*3,p+1)
    
for s in range(1,65):
    if f1(s,0):
        print(s)
    
