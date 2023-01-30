s = open('/home/diana/ЕГЭ/пробник 11.2022/17 (7).txt')
a = [int(i) for i in s]

minn =40


count = 0
summs = []
numb = []
mins = 10**10   
for i in range(len(a)-1):
    summ = a[i] + a[i+1]
    if a[i]%minn == 0 and a[i+1]%minn == 0:
        summs+=[summ]
        numb+=[[a[i],a[i+1]]]
# print(set(summs))

for i in range(len(numb)):
    if numb[i][0]+numb[i][1] == min(summs):
        print(max(numb[i]))

