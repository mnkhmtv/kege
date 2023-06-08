s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2309.txt')
nums = [int(i) for i in s]

ans11 = []
ans17 = []

for i in nums:
    if i % 11 == 0:
        ans11.append(i)
    elif i % 17 == 0:
        ans17.append(i)

if len(ans17) > len(ans11):
    print(len(ans17), max(ans17))
elif len(ans11) > len(ans17):
    print(len(ans11), min(ans11))
