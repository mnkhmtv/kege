s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_2399.txt')
nums = [int(i) for i in s]

s35 = 0
for i in nums:
    if i % 35 == 0:
        s35 += sum(map(int, str(i)))
# print(s35)
count = 0
mn = 1e9

for i in range(len(nums) - 1):
    h1 = hex(nums[i])[-2:]
    h2 = hex(nums[i+1])[-2:]
    if (nums[i] > s35 and nums[i+1] <= s35 and h2 == 'ef' and h1 != 'ef') or \
    (nums[i+1] > s35 and nums[i] <= s35 and h1 == 'ef' and h2 != 'ef'):
        count += 1
        mn = min(mn, nums[i] + nums[i+1])
print(count, mn)