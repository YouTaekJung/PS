n, m = int(input()), int(input())
s = set(map(str, range(10)))
if m != 0:
    s -= set(input().split())

ans = abs(n - 100)
for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if num[i] not in s:
            break
        elif i == len(num) - 1:
            ans = min(ans, abs(n - int(num)) + len(str(num)))

print(ans)