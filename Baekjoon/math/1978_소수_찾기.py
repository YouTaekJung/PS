n = int(input())
nums = list(map(int, input().split()))
res = 0
for num in nums:
    if num == 2:
        res += 1
    for i in range(2, num):
        if num % i == 0:
            break
        if i == num - 1:
            res += 1
print(res)