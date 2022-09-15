n = int(input())
li = sorted(list(map(int, input().split())))

ans = 0
for cur in range(n):
    temp = li[:cur] + li[cur + 1:]
    left, right = 0, len(temp) - 1
    while left < right:
        if temp[left] + temp[right] == li[cur]:
            ans += 1
            break
        if temp[left] + temp[right] < li[cur]:
            left += 1
        else:
            right -= 1
print(ans)