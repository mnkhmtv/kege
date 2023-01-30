# +1/+2/*2 ob = 60  >=51 1<=s<=50

def f(s,ost,p):
    if p == 3 and s>=51:
        return 1
    elif p == 3 and s<51:
        return 0
    elif p<3 and s>=51:
        return 0
    
    if p%2==0 and ost<=30:
        return f(s*2,ost-s,p+1) or f(s+1,ost-1,p+1) or f(s+2,ost-2,p+1)
    elif p%2!=0 and ost>30:
        return f(s+1,ost-1,p+1) or f(s+2,ost-2,p+1)
    elif p%2==0 and ost<=30:
        return f(s*2,ost-s,p+1) and f(s+1,ost-1,p+1) and  f(s+2,ost-2,p+1)
    elif p%2==0 and ost>30:
        return f(s+1,ost-1,p+1) and f(s+2,ost-2,p+1)
    
for s in range(1,51):
    if f(s,60,0)==1:
        print(s)