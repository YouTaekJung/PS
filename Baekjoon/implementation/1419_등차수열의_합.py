l, r, k = int(input()), int(input()), int(input())
ans = set()
for i in range(1, r // k + 1):
    j = 1
    while True:
        cur = k * i + k * (k - 1) * j / 2
        if cur > r:
            break
        if l <= cur <= r:
            ans.add(cur)
        j += 1
print(len(ans))