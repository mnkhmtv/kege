s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2310.txt')
nums = [int(i) for i in s]

an4 = []
for i in nums:
    if i % 10 == 4:
        an4.append(i)
smx = min(an4) + max(an4)

mx = count = 0
for i in range(len(nums) - 1):
    sm = nums[i] + nums[i+1]
    if sm < smx:
        count += 1
        mx = max(mx, sm)
print(count, mx)



