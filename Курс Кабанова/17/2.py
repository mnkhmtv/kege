s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2013.txt')
nums = [int(i) for i in s]
count = 0
mn = 1e9
for i in nums:
    if (i % 10 == 2 or i % 10 == 7) and i % 3 == 0 and i % 11 == 0:
        count += 1
        mn = min(mn, i)
print(count, mn)