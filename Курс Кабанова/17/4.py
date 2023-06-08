s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2016.txt')
nums = [int(i) for i in s]

ans = []
for i in nums:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        ans.append(i)

print(len(ans), max(ans) - min(ans))
