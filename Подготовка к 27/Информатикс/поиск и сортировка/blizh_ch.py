N = int(input())
a = [int(i) for i in input().split()]
x = int(input())

numb = a[0]
for i in a:
    if abs(x - numb) > abs(x - i):
        numb = i

print(numb)