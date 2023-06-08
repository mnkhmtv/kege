s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2015.txt')
nums = [int(i) for i in s]

ans = []

for i in nums:
    if (i % 10 == 5 or i % 10 == 7) and i % 9 != 0 and i % 11 != 0:
        ans.append(i)
print(len(ans), min(ans) + max(ans))
 