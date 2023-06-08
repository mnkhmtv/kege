s = open('/home/diana/ЕГЭ/Курс Кабанова/17/17_1994.txt')
nums = [int(i) for i in s]
print(nums)
count = 0
mn = 1e9

for i in range(len(nums) - 1):
    summ = nums[i] + nums[i+1]
    pr = nums[i] * nums[i+1]
    if abs(summ) % 7 == 0 and pr > 0:
        count += 1
        mn = min(mn, pr)
print(count, mn)