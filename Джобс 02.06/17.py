s = open('/home/diana/ЕГЭ/Джобс 02.06/17_8954.txt')
nums = [int(i) for i in s]

mx = 0
for i in nums:
    hx = hex(i)[2:]
    if hx[-2:] == '0f':
        mx = max(mx, i)
print(mx)
k = 0
mxs = 0
for i in range(len(nums) - 1):
    if (nums[i] % 7 == 0 and nums[i+1] % 7 != 0 and (nums[i] + nums[i+1]) % mx == 0) \
        or (nums[i+1] % 7 == 0 and nums[i] % 7 != 0 and (nums[i] + nums[i+1]) % mx == 0):
        k += 1
        mxs = max(mxs, nums[i] + nums[i+1])
print(k, mxs)

