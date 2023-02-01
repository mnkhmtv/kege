N = int(input())
a = [int(i) for i in input().split()]
x = int(input())

count = 0
for i in a:
    if i == x:
        count += 1

if count >= 1:
    print('YES')
else: 
    print('NO')