s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2238.txt')
nums = [int(i) for i in s]

count = mx = 0
sr_ar = sum(nums) / len(nums)

for i in range(len(nums) - 2):
    if (nums[i] > sr_ar and nums[i + 1] > sr_ar) or \
    (nums[i] > sr_ar and nums[i + 2] > sr_ar) or \
    (nums[i + 1] > sr_ar and nums[i + 2] > sr_ar):
        count += 1
        mx = max(mx, nums[i] + nums[i+1] + nums[i+2])
print(count, mx)