s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2239.txt')
nums = [int(i) for i in s]

mx19 = 0
for i in nums:
    if i % 19 == 0:
        mx19 = max(mx19, i)

count = 0
mn = 1e9

for i in range(len(nums) - 1):
    sm = nums[i] + nums[i+1]
    if nums[i] > mx19 or nums[i+1] > mx19:
        count += 1
        mn = min(mn, sm)
print(count, mn)