s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2002.txt')
nums = [int(i) for i in s]

count = 0
mn = 1e9

for i in range(len(nums) - 3):
    rsn = max(nums[i], nums[i+1], nums[i+2], nums[i+3]) - min(nums[i], nums[i+1], nums[i+2], nums[i+3])
    sm = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
    if rsn > 1000 and (nums[i] > nums[i+1] > nums[i+2] > nums[i+3]):
        count += 1
        mn = min(mn, sm)
print(count, mn)