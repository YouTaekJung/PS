a, b = map(int, input().split())
ans = [0, 0]

while a > 1 or b > 1:
    if a > b:
        a -= b
        ans[0] += 1
    else:
        b -= a
        ans[1] += 1

print(*ans)