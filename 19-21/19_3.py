#+1 *3 >=66 1<=s<=65
def f(s,p):
    if s>=66 and p ==2:
        return 1
    elif s>= 66 and p!=0:
        return 0
    elif s<66 and p == 2:
        return 0
    return f(s+1,p+1) + f(s*3,p+1)

for s in range(1,66):
    if f(s,0):
        print(s)
        input()