s = open('/home/diana/ЕГЭ/24/24.txt').readline()
# print(s)
k = 0
maxx = 0

s = s.replace('AB','1')
# print(s)

for i in range(len(s)-1):
    
    if s[i] == '1':
        k+=2

        if s[i+1] == 'A':
            k+=1

        if k>maxx:
            maxx = k
            
    else:
        k = 0

print(maxx)

