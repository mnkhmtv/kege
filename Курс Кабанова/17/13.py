s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2401.txt')
nums = [int(i) for i in s]

count = 0
mn = 1e9

for i in range(len(nums) - 1):
    smod = abs(nums[i]) + abs(nums[i+1])
    if 50 <= smod <= 200:
        count += 1
        mn = min(mn, nums[i], nums[i+1])
print(count, mn)