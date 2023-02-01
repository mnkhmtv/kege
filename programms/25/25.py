# Пусть M(N)  — сумма двух наибольших различных натуральных делителей натурального числа N,
#  не считая самого числа. Если у числа N меньше двух таких делителей, то M(N) считается равным 0.

# Найдите 5 наименьших натуральных чисел, превышающих 10 000 000, для которых 0 < M(N) < 10 000.
#  В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.
delitelies = set()
# def deliteli(n,m):
#     if m!=0 and n%m==0  and n!=m:
#         return m
        
# all = []
# summ = 0
# d=[]
# for n in range(10000000,100000000):
#     for m in range(int(n**0.5)+1):
        
#         if deliteli(n,m)!=None:
#             if (n**0.5) == deliteli(n,m)**2:
#                 d+=[deliteli(n,m)]
#             else:
#                 d+=[deliteli(n,m)]+[n//deliteli(n,m)]
#         # print(d)
        
#         if len(d)>=2:
#             summ = d[-1]+d[-2]
#             if summ<10000:
#                 all+=[summ]
                
                        
            

# print(all[:5])
deliteli = []
all = []
summ = 0
for n in range(10000000,100000000):
    deliteli = []
    for m in range(2,int(n**0.5)+1):
        if n == m*m:
            deliteli+=[m]
        elif n%m == 0:
            deliteli+=[m]+[n//m]
    
    deliteli = sorted(deliteli)

    if len(deliteli)>=2:
        summ = deliteli[-1]+deliteli[-2]
        if summ<=10000:
            # all+=[summ]
            print(summ)
# print(all[:5])






