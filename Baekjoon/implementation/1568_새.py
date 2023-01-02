n = int(input())
ans = 0
i = 1

while n > 0:
    if n < i:
        i = 1
    n -= i
    i += 1
    ans += 1

print(ans)