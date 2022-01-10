n, m = map(int, input().split())
nums = list(map(int, input().split()))
max_num = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            sum_num = nums[i] + nums[j] + nums[k]
            if sum_num <= m and sum_num > max_num:
                max_num = sum_num
print(max_num)